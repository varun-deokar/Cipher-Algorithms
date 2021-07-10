import random
import math


def input_function():
    prime_numbers = []
    for i in range(10000, 100000):
        j = 2
        while j <= math.sqrt(i):
            if i % j == 0:
                break
            j += 1
        else:
            prime_numbers.append(i)
    public_key_1 = prime_numbers[random.randint(0, len(prime_numbers))]
    while True:
        public_key_2 = prime_numbers[random.randint(0, len(prime_numbers))]
        if public_key_1 != public_key_2:
            break
    private_key_1 = random.randint(1, 10000)
    private_key_2 = random.randint(1, 10000)
    return public_key_1, public_key_2, private_key_1, private_key_2


def key_generation(p, g, a, b):
    key_1 = (g ** a) % p
    key_2 = (g ** b) % p
    return key_1, key_2


def key_exchange(x, y, p, a, b):
    ka = y ** a % p
    kb = x ** b % p
    if ka == kb:
        print("Common Key Generated is ", ka)


def main():
    public_key_1, public_key_2, private_key_1, private_key_2 = input_function()
    x, y = key_generation(public_key_1, public_key_2, private_key_1, private_key_2)
    key_exchange(x, y, public_key_1, private_key_1, private_key_2)


if __name__ == "__main__":
    main()
