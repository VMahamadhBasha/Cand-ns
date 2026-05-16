from Crypto.Cipher import ARC4
import base64

key = input("Enter key : ").encode()

text = input("Enter text : ")

cipher = ARC4.new(key)

# Encryption
encrypted = cipher.encrypt(text.encode())

emsg = base64.b64encode(encrypted).decode()

print("Encrypted :", emsg)

# Decryption
decoded = base64.b64decode(emsg)

decrypted = cipher.decrypt(decoded).decode()

print("Decrypted :", decrypted)
