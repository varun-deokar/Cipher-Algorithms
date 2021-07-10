import random
import math


def input_function():
    coprime_arr = []
    message = input("Enter a string\n")
    for i in range(1, 10000):
        if math.gcd(i, 95) == 1:
            coprime_arr.append(i)
    key1 = coprime_arr[random.randint(0, len(coprime_arr))]
    key2 = random.randint(0, 10000)
    print("\nRandom keys generated are", key1, key2)
    return message, key1, key2


def encrypt(message, key1, key2):
    result = ""
    for i in message:
        result += chr(((ord(i) - 32) * key1 + key2) % 95 + 32)
    print("\nEncrypted message is " + "\" " + result + " \"")
    return result


def decrypt(message, key1, key2):
    result = ""
    key1_inv = 0
    for i in range(95):
        if (key1 * i) % 95 == 1:
            key1_inv = i
            print("\nKey1 inverse is", key1_inv)
            break
    for i in message:
        result += chr(((ord(i) - 32 - key2) * key1_inv) % 95 + 32)
    print("\nDecrypted message is " + "\" " + result + " \"")


def main():
    message, key1, key2 = input_function()
    encrypted_message = encrypt(message, key1, key2)
    decrypt(encrypted_message, key1, key2)


if __name__ == "__main__":
    main()
