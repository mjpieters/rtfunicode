# Encode unicode strings to RTF 1.5-compatible command codes.
# Command codes are of the form `\uN?`, where N is a signed 16-bit integer and
# ? is a placeholder character for pre-1.5 RTF readers.

import codecs
import re
import sys

from struct import unpack


if sys.version_info[0] < 3 and sys.maxunicode == (2 ** 16 - 1):
    # Python 2 UCS 2 build
    # Encode everything < 0x20, the \, { and } chars and everything > 0x7f
    # codepoints over sys.maxunicode are already encoded to surrogates so match
    # those explicitly.
    _charescape = re.compile(
        u'([\x00-\x1f\\\\{}\x80-\ud7ff\ue000-\uffff])|'
        u'([\ud800-\udbff][\udc00-\udfff])')

else:
    # Python 3
    # Encode everything < 0x20, the \, { and } chars and everything > 0x7f.
    # Codeponts over \uffff are handled separately so capture these in a second
    # group. Valid surrogate pairs are supported too.
    _charescape = re.compile(
        u'([\x00-\x1f\\\\{}\x80-\ud7ff\ue000-\uffff])|'
        u'([\U00010000-\U0001ffff]|[\ud800-\udbff][\udc00-\udfff])')


def _replace(match):
    # Convert codepoint into a signed integer
    char = match.group(1)
    if not char:
        # Encoding to UTF-16 is the simplest path to supporting surrogates.
        encoded = match.group(2).encode('utf-16-le')
        cp1, cp2 = unpack('<hh', encoded)
        # Microsoft RTF 1.9.1 specification (Word 2007), page 115, all
        # surrogates must be wrapped in a {/mr...} math text-run group.
        # Experimentation with various RTF apps (Word, Apple TextEdit,
        # LibreOffice) shows surrogates work in regular paragraphs too.
        return u'\\u%d?\\u%d?' % (cp1, cp2)
    cp = ord(char)
    return u'\\u%d?' % (cp > 32767 and cp - 65536 or cp,)


def _rtfunicode_encode(text, errors):
    # Encode to RTF \uDDDDD? signed 16 integers and replacement char
    return _charescape.sub(_replace, text).encode('ascii', errors)


class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return _rtfunicode_encode(input, errors), len(input)

try:
    class IncrementalEncoder(codecs.IncrementalEncoder):
        def encode(self, input, final=False):
            return _rtfunicode_encode(input, self.errors)
except AttributeError:
    # Python 2.4, ignore
    pass


class StreamWriter(Codec, codecs.StreamWriter):
    pass


def rtfunicode(name):
    if name == 'rtfunicode':
        try:
            return codecs.CodecInfo(
                name='rtfunicode',
                encode=Codec().encode,
                decode=Codec().decode,  # raises NotImplementedError
                incrementalencoder=IncrementalEncoder,
                streamwriter=StreamWriter,
            )
        except AttributeError:
            # Python 2.4
            return (Codec().encode, Codec().decode, StreamWriter, None)

codecs.register(rtfunicode)
