def input_function():
    message = input("Enter a string\n")
    key = input("Enter a key\n")
    return message, key


def key_generation(message, key):
    new_key = ""
    size = len(key)
    for i in range(len(message)):
        new_key = new_key + key[i % size]
    return new_key


def encrypt(message, key):
    result = ""
    for i, j in zip(message, key):
        result += chr((ord(i) - 32 + ord(j) - 32) % 95 + 32)
    print("\nEncrypted message is " + "\" " + result + " \"")
    return result


def decrypt(message, key):
    result = ""
    for i, j in zip(message, key):
        result += chr((ord(i) - 32 - (ord(j) - 32)) % 95 + 32)
    print("\nDecrypted message is " + "\" " + result + " \"")


def main():
    message, key = input_function()
    key = key_generation(message, key)
    encrypted_message = encrypt(message, key)
    decrypt(encrypted_message, key)


if __name__ == "__main__":
    main()