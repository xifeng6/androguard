import unittest

import sys
from xml.dom import minidom

PATH_INSTALL = "./"
sys.path.append(PATH_INSTALL)

from androguard.core.bytecodes import apk


class AXMLTest(unittest.TestCase):
    def testAXML(self):
        filenames = [
            "examples/axml/AndroidManifest-Chinese.xml",
            "examples/axml/AndroidManifest-xmlns.xml",
            "examples/axml/AndroidManifest.xml", "examples/axml/test.xml",
            "examples/axml/test1.xml", "examples/axml/test2.xml",
            "examples/axml/test3.xml"
        ]

        for filename in filenames:
            with open(filename, "rb") as fd:
                ap = apk.AXMLPrinter(fd.read())
                self.assertIsNotNone(ap)

                e = minidom.parseString(ap.get_buff())
                self.assertIsNotNone(e)

    def testNonZeroStyleOffset(self):
        """
        Test if a nonzero style offset in the string section causes problems
        if the counter is 0
        """
        filename = "examples/axml/AndroidManifestNonZeroStyle.xml"

        with open(filename, "rb") as f:
            ap = apk.AXMLPrinter(f.read())
        self.assertIsInstance(ap, apk.AXMLPrinter)

        e = minidom.parseString(ap.get_buff())
        self.assertIsNotNone(e)

    def testExtraNamespace(self):
        """
        Test if extra namespaces cause problems
        """
        filename = "examples/axml/AndroidManifestExtraNamespace.xml"

        with open(filename, "rb") as f:
            ap = apk.AXMLPrinter(f.read())
        self.assertIsInstance(ap, apk.AXMLPrinter)

        e = minidom.parseString(ap.get_buff())
        self.assertIsNotNone(e)

    def testExtraNamespace(self):
        """
        Assert that files with a broken filesize are not parsed
        """
        filename = "examples/axml/AndroidManifestWrongFilesize.xml"

        with self.assertRaises(AssertionError) as cnx:
            with open(filename, "rb") as f:
                apk.AXMLPrinter(f.read())
        self.assertTrue("Declared filesize does not match" in str(cnx.exception))


if __name__ == '__main__':
    unittest.main()
