from cs50 import get_string
from sys import argv


def main():
    # TODO
    while True:
        if len(argv) == 2:
            message = get_string("What message would you like to censor?\n")

            # read file line by line and remove the \n
            bannedWords = set(line.strip('\n') for line in open(argv[1]))

            # censorMessage method replaces the band words with *
            print(censorMessage(message, bannedWords))

            exit(0)

        else:
            print("Usage: python bleep.py dictionary")
            exit(1)


def censorMessage(message, bannedWords):
    # create array of words in message string
    words = message.split()
    for word in words:
        # Check if the word is one of the banned words
        if word.lower() in bannedWords:
            # replace the word with *
            censoredString = ('*')*(len(word))
            message = message.replace(word, censoredString)

    return message


if __name__ == "__main__":
    main()
