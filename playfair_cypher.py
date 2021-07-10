def input_function():
    message = input("Enter a message\n")
    key = input("Enter a key\n")
    message = message.lower()
    message = message.replace('j', 'i')
    key = key.lower()
    return message, key


def playfair_key_generation(key):
    key = key.replace("j", "i")
    a = 'a'
    row, col = (5, 5)
    matrix_key = [[None] * col for i in range(row)]
    i, j, c = 0, 0, -1
    while i < 5:
        j = 0
        while j < 5:
            c += 1
            if c == len(key):
                while a <= 'z':
                    if a == 'j':
                        j -= 1
                    else:
                        for b in matrix_key:
                            if a in b:
                                j -= 1
                                break
                        else:
                            matrix_key[i][j] = a
                    if j == 4:
                        i += 1
                        j = 0
                    else:
                        j += 1
                    a = chr(ord(a) + 1)
                break
            for k in range(i + 1):
                if key[c] in matrix_key[k]:
                    j -= 1
                    break
            else:
                matrix_key[i][j] = key[c]
            j += 1
        if c == len(key):
            break
        i += 1
    print("\n", matrix_key)
    return matrix_key


def encrypt(text, key):
    encrypted_text, message, var1, var2, count = "", text[0], text[0], "", 1
    c, j = 1, 0
    for i in range(1, len(text)):
        if count % 2 == 0:
            var1 = text[i]
            message = message + text[i]
        else:
            var2 = text[i]
            if var1 == var2:
                message = message + 'x' + text[i]
            else:
                message = message + text[i]
        count += 1
    print(message)

    if not len(message) % 2 == 0:
        message = message + 'x'
    for i in message:
        c += 1
        if c % 2 == 0:
            temp = i
            continue
        else:
            j = 0
            while j < 5:
                if i in key[j]:
                    row_loc_2 = j
                    col_loc_2 = key[j].index(i)
                if temp in key[j]:
                    row_loc_1 = j
                    col_loc_1 = key[j].index(temp)
                j += 1

            if row_loc_1 == row_loc_2:
                encrypted_text = encrypted_text + key[row_loc_1][(col_loc_1 + 1) % 5] + key[row_loc_2][(col_loc_2 + 1) % 5]
            elif col_loc_1 == col_loc_2:
                encrypted_text = encrypted_text + key[(row_loc_1 + 1) % 5][col_loc_1] + key[(row_loc_2 + 1) % 5][col_loc_2]
            else:
                encrypted_text = encrypted_text + key[row_loc_1][col_loc_2] + key[row_loc_2][col_loc_1]

    print("\nEncrypted message is " + "\" " + encrypted_text + " \"")
    return encrypted_text


def decrypt(message, key):
    decrypted_text = ""
    c, j = 1, 0
    for i in message:
        c += 1
        if c % 2 == 0:
            temp = i
            continue
        else:
            j = 0
            while j < 5:
                if i in key[j]:
                    row_loc_2 = j
                    col_loc_2 = key[j].index(i)
                if temp in key[j]:
                    row_loc_1 = j
                    col_loc_1 = key[j].index(temp)
                j += 1

            if row_loc_1 == row_loc_2:
                decrypted_text = decrypted_text + key[row_loc_1][(col_loc_1 - 1) % 5] + key[row_loc_2][(col_loc_2 - 1) % 5]
            elif col_loc_1 == col_loc_2:
                decrypted_text = decrypted_text + key[(row_loc_1 - 1) % 5][col_loc_1] + key[(row_loc_2 - 1) % 5][col_loc_2]
            else:
                decrypted_text = decrypted_text + key[row_loc_1][col_loc_2] + key[row_loc_2][col_loc_1]

    print("\nDecrypted message is " + "\" " + decrypted_text + " \"")


def main():
    message, key = input_function()
    matrix_key = playfair_key_generation(key)
    encrypted_message = encrypt(message, matrix_key)
    decrypt(encrypted_message, matrix_key)


if __name__ == "__main__":
    main()
