# ChaCha20-Poly1305 Encryption and Decryption Example

This repository contains a Python script that demonstrates the use of the ChaCha20-Poly1305 authenticated encryption algorithm for encrypting and decrypting data.

## Description

ChaCha20-Poly1305 is a powerful cryptographic algorithm that provides both confidentiality and integrity protection for data. It is a combination of the ChaCha20 stream cipher and the Poly1305 message authentication code (MAC).

This script uses the `ChaCha20Poly1305` cipher from the `cryptography` library to perform the encryption and decryption operations. It generates a random 32-byte key and a random 12-byte nonce, then uses these to encrypt a sample plaintext message and decrypt the resulting ciphertext.

## Usage

1. Ensure you have Python 3 installed on your system.
2. Install the `cryptography` library by running the following command:
   ```
   pip install cryptography
   ```
3. Save the provided Python script to a file (e.g., `chacha20_poly1305.py`).
4. Run the script:
   ```
   python chacha20_poly1305.py
   ```
5. The script will output the original plaintext, the encrypted ciphertext, and the decrypted plaintext.

## Example Output

```
Plaintext: This is a secret message.
Ciphertext: b'X\xf9\x1b\x18\xaa\xb3\xd9\xd3H\xd2\x81\xc0\xdeb\x8a\x8a\xc9\xdf\xf0\xb4j\x83P3\x1a'
Decrypted Plaintext: This is a secret message.
```
