import hashlib

try:
    # User input
    text = input("Enter the text: ")

    # Convert text into bytes
    data = text.encode()

    # Create SHA-1 hash object
    sha1 = hashlib.sha1()

    # Update hash object with data
    sha1.update(data)

    # Generate hexadecimal hash value
    hash_value = sha1.hexdigest()

    # Output
    print("\nSHA-1 Hash Function")
    print("----------------------")
    print("Original Text :", text)
    print("SHA-1 Hash    :", hash_value)

except Exception as e:
    print("Error:", e)
