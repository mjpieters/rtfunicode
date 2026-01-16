import string
import unittest


class RTFUnicodeTests(unittest.TestCase):
    def setUp(self):
        import rtfunicode as rtfunicode  # auto-registers

    def _compare(self, in_, out):
        self.assertEqual(in_.encode("rtfunicode"), out)

    def testPlainASCII(self):
        ascii = string.ascii_letters + string.digits
        self._compare(ascii, ascii.encode())

    def testRTFControlCodes(self):
        self._compare("\\{}", b"\\u92?\\u123?\\u125?")

    def testLatin1(self):
        self._compare("\xe0\xeb", b"\\u224?\\u235?")

    def testBMP(self):
        self._compare("\u0123\u8123", b"\\u291?\\u-32477?")

    def testBeyondBMP(self):
        # RTF 1.9.1 (Word 2007), page 115 states that surrogate pairs are
        # supported in math text-run groups; experimentation with Word shows
        # they can exist outside of these too.
        testChar = "\U00010196"
        self._compare(testChar, b"\\u-10240?\\u-8810?")


if __name__ == "__main__":
    unittest.main()
