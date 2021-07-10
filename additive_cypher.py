import random
import math

def input_function():
    message = input("Enter a string\n")
    key = math.ceil((random.random() + 0.0001) * 10000)
    print("\nRandom key generated is", key)
    return message, key


def encrypt(message, key):
    result = ""
    for i in message:
        result += chr((ord(i) - 32 + key) % 95 + 32)
    print("\nEncrypted message is " + "\" " + result + " \"")
    return result


def decrypt(message, key):
    result = ""
    for i in message:
        result += chr((ord(i) - 32 - key) % 95 + 32)
    print("\nDecrypted message is " + "\" " + result + " \"")


def main():
    message, key = input_function()
    encrypted_message = encrypt(message, key)
    decrypt(encrypted_message, key)


if __name__ == "__main__":
    main()