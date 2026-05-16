from Crypto.Cipher import Blowfish
import base64

key = input("Enter key : ").encode()

text = input("Enter text : ")

while len(text) % 8 != 0:
    text += " "

cipher = Blowfish.new(key, Blowfish.MODE_ECB)

# Encryption
encrypted = cipher.encrypt(text.encode())

emsg = base64.b64encode(encrypted).decode()

print("Encrypted :", emsg)

# Decryption
decoded = base64.b64decode(emsg)

decrypted = cipher.decrypt(decoded).decode()

print("Decrypted :", decrypted)
