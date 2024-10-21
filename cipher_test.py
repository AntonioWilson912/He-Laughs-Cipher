import unittest
from cipher import VigenereCipher

class CipherTest(unittest.TestCase):
    """
    Unit tests for the VigenereCipher class.

    This class contains tests for the encoding and decoding functionality of
    the Vigenère cipher implementation.
    """

    def setUp(self):
        """
        Set up the test case by creating an instance of VigenereCipher.

        This method is called before each test method to prepare the environment.
        """
        self.cipher = VigenereCipher()
        return super().setUp()

    def test_encode(self):
        """
        Test the encoding method of the VigenereCipher class.

        This method verifies that the encode function correctly encrypts messages
        with the specified keys and raises a ValueError for invalid keys.
        """
        self.assertEqual(self.cipher.encode("The", "THE"), "Moi")
        self.assertEqual(self.cipher.encode("The dog jumped.", "XML"), "Qtp aar ggxmqo.")
        self.assertEqual(
            self.cipher.encode(
                "Once you complete this assessment and have been deemed worthy, "
                "there will be an additional monetary gift. Gifts are not just given. "
                "They must be earned.", 
                "STEAM"
            ),
            "Ggge kgn goyheitq lams mkliseexrt mfw lahw uiez vximqv psrfzr, "
            "xhqjx aixd ui az swhifahrax ehrefskc guxm. Kirll erq fhx jgkm kihwg. "
            "Xhqq fysf tx iadfxh."
        )
        with self.assertRaises(ValueError):
            self.cipher.encode("Failed message.", "Bad key.")

    def test_decode(self):
        """
        Test the decoding method of the VigenereCipher class.

        This method verifies that the decode function correctly decrypts messages
        with the specified keys and raises a ValueError for invalid keys.
        """
        self.assertEqual(self.cipher.decode("Moi", "THE"), "The")
        self.assertEqual(self.cipher.decode("Qtp aar ggxmqo.", "XML"), "The dog jumped.")
        self.assertEqual(
            self.cipher.decode(
                "Ggge kgn goyheitq lams mkliseexrt mfw lahw uiez vximqv psrfzr, "
                "xhqjx aixd ui az swhifahrax ehrefskc guxm. Kirll erq fhx jgkm kihwg. "
                "Xhqq fysf tx iadfxh.", 
                "STEAM"
            ),
            "Once you complete this assessment and have been deemed worthy, "
            "there will be an additional monetary gift. Gifts are not just given. "
            "They must be earned."
        )
        with self.assertRaises(ValueError):
            self.cipher.decode("Qtp aar ggxmqo.", "Bad key.")

if __name__ == "__main__":
    unittest.main()
