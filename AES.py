from Crypto.Cipher import AES
import base64

key = input("Enter 16 character key : ").encode()

text = input("Enter text : ")

while len(text) % 16 != 0:
    text += " "

cipher = AES.new(key, AES.MODE_ECB)

# Encryption
encrypted = cipher.encrypt(text.encode())

emsg = base64.b64encode(encrypted).decode()

print("Encrypted :", emsg)

# Decryption
decoded = base64.b64decode(emsg)

decrypted = cipher.decrypt(decoded).decode()

print("Decrypted :", decrypted)
