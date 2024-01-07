# PyEncryptTools

PyEncryptTools is a Python package that provides a set of simple tools for text encryption and decryption. The package includes functions for basic encryption algorithms, allowing users to easily encrypt and decrypt messages or files.

## Features

- **Caesar Cipher**: Implements a Caesar cipher encryption and decryption function, allowing users to shift characters by a specified key.
- **Substitution Cipher**: Creates a substitution cipher encryption and decryption function, replacing each character with a corresponding substitute based on a given key.
- **Vigenère Cipher**: Implements a Vigenère cipher encryption and decryption function, allowing users to use a keyword to encrypt and decrypt messages.
- **Base64 Encoding/Decoding**: Provides functions for base64 encoding and decoding, useful for encoding binary data or files.
- **Random Key Generator**: Includes a function to generate random keys for encryption algorithms, ensuring secure and varied keys for users.

## Installation

To install PyEncryptTools directly from the GitHub repository, run the following command:

```bash
pip install git+https://github.com/hackifiery/PyEncryptTools.git
```
Please note that this requires Git to be installed on your system.
## Usage

Here's a simple usage example:

```python
from PyEncryptTools import caesar_cipher, random_key_generator
```

Generate a random key of length 10
```python
key = random_key_generator(10)
```
Use the key to encrypt a message
```python
encrypted_message = caesar_cipher('Hello, world!', key, 'e') print(encrypted_message)
```
Decrypt the message
``` python
decrypted_message = caesar_cipher(encrypted_message, key, 'd') print(decrypted_message)
```
