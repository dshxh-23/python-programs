from cryptography.fernet import Fernet

# Generating a key
key = Fernet.generate_key()     # Generating a random 32-byte encryption key 
cipher = Fernet(key)            # Create a Fernet encryption object using the random key generated, thus providing encrypt() and decrypt methods tied to that key

# Encrypting a msg
message = "This is a secret".encode()   # Converting a string object to bytes using the encode() function. Necessary for encrypting and decrypting
token = cipher.encrypt(message)         # Encrypting the message

original = cipher.decrypt(token)

print("Key:", key)
print("Encrypted:", token)
print("Decrypted:", original.decode())