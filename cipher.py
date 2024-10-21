class VigenereCipher:
    """
    A class that implements the Vigenère cipher for encoding and decoding messages.
    
    The Vigenère cipher is a method of encrypting alphabetic text by using a simple 
    form of polyalphabetic substitution. It uses a keyword to determine the shift for 
    each letter of the plaintext message.
    
    Attributes:
        START_UPPER (int): ASCII value of 'A' (65).
        START_LOWER (int): ASCII value of 'a' (97).
        NUM_LETTERS (int): Total number of letters in the English alphabet (26).
    """

    START_UPPER = 65
    START_LOWER = 97
    NUM_LETTERS = 26

    def encode(self, message: str, key: str) -> str:
        """
        Encode a message using the Vigenère cipher.

        Args:
            message (str): The plaintext message to encode.
            key (str): The keyword used for encoding, which should contain only letters.

        Returns:
            str: The encoded ciphertext.

        Raises:
            ValueError: If the key contains non-alphabetic characters.
        """
        key_index = 0
        encoded_msg = ""
        key = key.upper()

        if not key.isalpha():
            raise ValueError("Key must only contain letters.")

        for i in range(len(message)):
            if message[i].isalpha():
                if message[i].isupper():
                    pos_let = ord(message[i]) - self.START_UPPER
                    pos_key = ord(key[key_index]) - self.START_UPPER
                    char = (pos_let + pos_key) % self.NUM_LETTERS + self.START_UPPER
                    if char == self.START_UPPER - 1:
                        char += self.NUM_LETTERS
                    encoded_msg += chr(char)
                else:
                    pos_let = ord(message[i]) - self.START_LOWER
                    pos_key = ord(key[key_index]) - self.START_UPPER
                    char = (pos_let + pos_key) % self.NUM_LETTERS + self.START_LOWER
                    if char == self.START_LOWER - 1:
                        char += self.NUM_LETTERS

                    encoded_msg += chr(char)
                key_index = (key_index + 1) % len(key)
            else:
                encoded_msg += message[i]
        return encoded_msg

    def decode(self, message: str, key: str) -> str:
        """
        Decode a message encoded with the Vigenère cipher.

        Args:
            message (str): The encoded ciphertext to decode.
            key (str): The keyword used for decoding, which should contain only letters.

        Returns:
            str: The decoded plaintext message.

        Raises:
            ValueError: If the key contains non-alphabetic characters.
        """
        key_index = 0
        decoded_msg = ""
        key = key.upper()
        
        if not key.isalpha():
            raise ValueError("Key must only contain letters.")
        for i in range(len(message)):
            if message[i].isalpha():
                if message[i].isupper():
                    pos_let = ord(message[i]) - self.START_UPPER + 1
                    pos_key = ord(key[key_index]) - self.START_UPPER
                    char = (pos_let - pos_key + 26) % self.NUM_LETTERS + self.START_UPPER - 1
                    decoded_msg += chr(char)
                else:
                    pos_let = ord(message[i]) - self.START_LOWER + 1
                    pos_key = ord(key[key_index]) - self.START_UPPER
                    char = (pos_let - pos_key + 26) % self.NUM_LETTERS + self.START_LOWER - 1
                    decoded_msg += chr(char)
                key_index = (key_index + 1) % len(key)
            else:
                decoded_msg += message[i]
        return decoded_msg

    
# cipher = VigenereCipher()
# msg = """Once you complete this assessment and have been deemed worthy, there will be an additional monetary gift. Gifts are not just given. They must be earned."""
# print(cipher.encode(msg, "STEAM"))
# msg = "ONCE YOU COMPLETE THIS ASSESSMENT AND HAVE BEEN DEEMED WORTHY, THERE WILL BE AN ADDITIONAL MONETARY GIFT. GIFTS ARE NOT JUST GIVEN. THEY MUST BE EARNED."
# print(cipher.encode(msg, "STEAM"))

# msg = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
# msg = cipher.encode(msg, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# print(msg)
# msg = cipher.decode(msg, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# print(msg)

# msg = "This is an encrypted message."
# msg = cipher.encode(msg, "KEY")
# print(msg)

# msg = cipher.decode(msg, "KEY")
# print(msg)