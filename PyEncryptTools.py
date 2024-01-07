def caesar_cipher(text, shift, mode='e'):
   result = ""
   if mode == 'e':
       for i in range(len(text)):
           char = text[i]
           if char.isupper():
               result += chr((ord(char) + shift - 65) % 26 + 65)
           else:
               result += chr((ord(char) + shift - 97) % 26 + 97)
   elif mode == 'd':
       for i in range(len(text)):
           char = text[i]
           if char.isupper():
               result += chr((ord(char) - shift - 65) % 26 + 65)
           else:
               result += chr((ord(char) - shift - 97) % 26 + 97)
   else:
       raise ValueError("Invalid mode. Mode must be either 'e' for encryption or 'd' for decryption.")
   return result

def substitution_cipher(text, key, mode='e'):
   if mode == 'e':
       result = ""
       for char in text:
           result += key[char]
   elif mode == 'd':
       result = ""
       for char in text:
           for k, v in key.items():
               if v == char:
                  result += k
   else:
       raise ValueError("Invalid mode. Mode must be either 'e' for encryption or 'd' for decryption.")
   return result

def vigenere_cipher(text, key, mode='e'):
   result = ""
   key_length = len(key)
   for i in range(len(text)):
       key_c = key[i % key_length]
       if mode == 'e':
           result += chr((ord(text[i]) + ord(key_c)) % 26 + 65)
       elif mode == 'd':
           result += chr((ord(text[i]) - ord(key_c)) % 26 + 65)
   return result

import base64

def base64_encode(data, mode='e'):
   if mode == 'e':
       return base64.b64encode(data)
   elif mode == 'd':
       return base64.b64decode(data)
   else:
       raise ValueError("Invalid mode. Mode must be either 'e' for encryption or 'd' for decryption.")
