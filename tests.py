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
        # There is documentation on how RTF should handle these
        # As such, this is unsupported by the library, but there
        # are some side-effects from using a UCS-2 build we can "test"
        testChar = '\U00010196'
        if len(u(testChar)) == 1:  # UCS-4 build
            self.assertRaises(
                UnicodeEncodeError,
                self._compare, testChar, 'ignored')
        elif ord(u(testChar)[0]) == 0xd800:  # Big-endian UTF-16
            # No idea if RTF will read this correctly at all
            # Windows is LE, so this is probably not going to fly.
            self._compare(testChar, '\\u-10240?\\u-8810?')
        else:
            # No idea if RTF will read this correctly at all
            # There is on documentation on how to encode a surrogate pair
            self._compare(testChar, '\\u-8810?\\u-10240?')


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
