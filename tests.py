import string
import sys
import unittest


# Python 2 and 3 compat.
if sys.version_info[0] < 3:
    u = lambda t: unicode(t.decode('unicode_escape'))
    b = str
else:
    u = lambda t: t
    b = lambda t: bytes(t, 'ascii')


class RTFUnicodeTests(unittest.TestCase):
    def setUp(self):
        import rtfunicode  # auto-registers
        rtfunicode         # pyflakes needn't worry

    def _compare(self, in_, out):
        self.assertEqual(u(in_).encode('rtfunicode'), b(out))

    def testPlainASCII(self):
        ascii = string.ascii_letters + string.digits
        self._compare(ascii, ascii)

    def testRTFControlCodes(self):
        self._compare('\\{}', '\\u92?\\u123?\\u125?')

    def testLatin1(self):
        self._compare('\xe0\xeb', '\\u224?\\u235?')

    def testBMP(self):
        self._compare('\u0123\u8123', '\\u291?\\u-32477?')

    def testBeyondBMP(self):
        # RTF 1.9.1 (Word 2007), page 115 states that surrogate pairs are
        # supported in math text-run groups; experimentation with Word shows
        # they can exist outside of these too.
        testChar = '\U00010196'
        self._compare(testChar, '\\u-10240?\\u-8810?')


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
