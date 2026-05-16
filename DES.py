from Crypto.Cipher import DES
import base64

key = input("Enter 8 character key : ").encode()

text = input("Enter text : ")

while len(text) % 8 != 0:
    text += " "

cipher = DES.new(key, DES.MODE_ECB)

# Encryption
encrypted = cipher.encrypt(text.encode())

emsg = base64.b64encode(encrypted).decode()

print("Encrypted :", emsg)

# Decryption
decoded = base64.b64decode(emsg)

decrypted = cipher.decrypt(decoded).decode()

print("Decrypted :", decrypted)
