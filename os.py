from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import os

# Generate a random 32-byte key
key = os.urandom(32)

# Generate a random 12-byte nonce
nonce = os.urandom(12)

# Plaintext to be encrypted
plaintext = b"This is a secret message."

# Encrypt the plaintext using ChaCha20-Poly1305
cipher = ChaCha20Poly1305(key)
ciphertext = cipher.encrypt(nonce, plaintext, associated_data=b"")

# Decrypt the ciphertext using ChaCha20-Poly1305
decrypted_plaintext = cipher.decrypt(nonce, ciphertext, associated_data=b"")

print("Plaintext:", plaintext.decode())
print("Ciphertext:", ciphertext)
print("Decrypted Plaintext:", decrypted_plaintext.decode())
