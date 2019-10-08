from sys import argv
from cs50 import get_string


def main():
    # check the number of command line arguments
    if len(argv) == 2:
        key = int(argv[1])
        # print(key)
        plaintext = get_string("plaintext: ")
        print("ciphertext: ", end="")
        print(encipher(plaintext, key))
        exit(0)
    else:
        print("Usage: ./caesar key")
        exit(1)


def encipher(text, key):
    cipherText = ""
    for i in range(len(text)):

        if text[i].isupper() == True:
            num = ord(text[i]) - ord('A')
            # Wrap around the alphabets between  A-Z
            cipherText += chr((num + key) % 26 + ord('A'))

        elif text[i].islower() == True:
            num = ord(text[i]) - ord('a')
            # Wrap around the alphabets between a-z
            cipherText += chr((num + key) % 26 + ord('a'))

        elif not text[i].isalpha():
            # preserve the character if not alphbetical
            cipherText += text[i]

        i += 1

    return cipherText


if __name__ == "__main__":
    main()
