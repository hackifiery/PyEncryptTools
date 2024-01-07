import unittest
from PyEncryptTools import caesar_cipher, substitution_cipher, vigenere_cipher, base64_encode, random_key_generator

class TestPyEncryptTools(unittest.TestCase):

   def test_caesar_cipher(self):
       self.assertEqual(caesar_cipher('hello', 3, 'e'), 'khoor')
       self.assertEqual(caesar_cipher('khoor', 3, 'd'), 'hello')

   def test_substitution_cipher(self):
       key = {'h':'j', 'e':'i', 'l':'o', 'o':'u'}
       self.assertEqual(substitution_cipher('hello', key, 'e'), 'jiouo')
       self.assertEqual(substitution_cipher('jiouo', key, 'd'), 'hello')

   def test_vigenere_cipher(self):
       self.assertEqual(vigenere_cipher('hello', 'key', 'e'), 'holwq')
       self.assertEqual(vigenere_cipher('holwq', 'key', 'd'), 'hello')

   def test_base64_encode(self):
       self.assertEqual(base64_encode('hello'.encode(), 'e'), b'aGVsbG8=')
       self.assertEqual(base64_encode(b'aGVsbG8=', 'd').decode(), 'hello')

   def test_random_key_generator(self):
       key = random_key_generator(5)
       self.assertEqual(len(key), 5)

if __name__ == '__main__':
   unittest.main()
