import numpy as np


def input_function():
    a, b, message = 0, -1, []
    text = input("Enter a string\n")
    # key = [[None] * len(text) for i in range(len(text))]
    for i in range(len(text)):
        message.append(ord(text[i]))
    # for i in range(len(text) ** 2):
    #     if i % len(text) == 0:
    #         a = 0
    #         b += 1
    #     key[a][b] = random.randint(0, 10000)
    #     a += 1
    message = np.array(message)
    key = np.array(([2, 2], [7, 8]))
    print("\nMessage = ", message)
    print("\nKey = ", key)
    return message, key


def encrypt(message, key):
    temp = ""
    encrypted_message = key @ message
    for i in range(len(encrypted_message)):
        temp = temp + chr(encrypted_message[i] % 95)
        encrypted_message[i] = encrypted_message[i] % 95
    print("\nEncrypted message is ", encrypted_message)
    print("\nEncrypted message is " + "\" " + temp + " \"")
    return encrypted_message


def decrypt(message, key):
    a, b, temp = 0, -1, ""
    inv_key = np.linalg.inv(key)
    det_key = round(np.linalg.det(key))
    print("\nDeterminant = ", det_key)
    inv_det = 0
    for i in range(95):
        if (det_key * i) % 95 == 1:
            inv_det = i
            break
    print(inv_det)

    adj_key = [[None] * len(message) for i in range(len(message))]
    key_mat = [[None] * len(message) for i in range(len(message))]
    for i in range(len(message) ** 2):
        if i % len(message) == 0:
            a = 0
            b += 1
        adj_key[a][b] = round(inv_key[a][b] * det_key) % 95
        a += 1
    print("\nAdjoint Key = ", adj_key)
    adj_key = np.array(adj_key)

    for i in range(len(message)):
        for j in range(len(message)):
            key_mat[i][j] = (adj_key[i][j] * inv_det) % 95
    print("\nKey Inverse = ", key_mat)

    key_mat = np.array(key_mat)
    decrypted_message = key_mat @ message
    print("\nDecrypted message = ", decrypted_message)
    for i in range(len(decrypted_message)):
        temp = temp + chr(decrypted_message[i] % 95 + 95)
        decrypted_message[i] = decrypted_message[i] % 95 + 95
    print("\nDecrypted message is " + "\" " + temp + " \"")
    print("\nDecrypted message is ", decrypted_message)


def main():
    message, key = input_function()
    encrypted_message = encrypt(message, key)
    decrypt(encrypted_message, key)


if __name__ == "__main__":
    main()