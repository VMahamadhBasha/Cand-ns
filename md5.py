import hashlib

try:
    # User input
    text = input("Enter the text: ")

    # Convert text into bytes
    data = text.encode()

    # Create MD5 hash object
    md5 = hashlib.md5()

    # Update hash object with data
    md5.update(data)

    # Generate hexadecimal hash value
    hash_value = md5.hexdigest()

    # Output
    print("\nMD5 Hash Function")
    print("----------------------")
    print("Original Text :", text)
    print("MD5 Hash      :", hash_value)

except Exception as e:
    print("Error:", e)
