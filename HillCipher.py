key = [[5, 8],
       [17, 3]]

inverse = [[9, 2],
           [1, 15]]

text = "HELLO"

# Padding
if len(text) % 2 != 0:
    text += "X"

encrypted = ""

# Encryption
for i in range(0, len(text), 2):

    a = ord(text[i]) - 65
    b = ord(text[i + 1]) - 65

    x = (a * key[0][0] + b * key[1][0]) % 26
    y = (a * key[0][1] + b * key[1][1]) % 26

    encrypted += chr(x + 65)
    encrypted += chr(y + 65)

print("Encrypted :", encrypted)


decrypted = ""

# Decryption
for i in range(0, len(encrypted), 2):

    a = ord(encrypted[i]) - 65
    b = ord(encrypted[i + 1]) - 65

    x = (a * inverse[0][0] + b * inverse[1][0]) % 26
    y = (a * inverse[0][1] + b * inverse[1][1]) % 26

    decrypted += chr(x + 65)
    decrypted += chr(y + 65)

print("Decrypted :", decrypted)
