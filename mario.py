from cs50 import get_int

def main():
    while True:
        height = get_int("Height: ")
        if height >= 1 and height <= 8:
            break

    gap = 2
    # japa()

    for i in range(1, height+1):
        # print the spaces to the left for that row
        print_spaces(height, i)
        # print the "#" for the row
        print_hashes(i)
        # Leave a gap in the middle of the row
        print_spaces(gap, 0)
        # print the "#" after the gap for that row
        print_hashes(i)
        # start the next row.
        print()


def print_spaces(height, row_number):
    for k in range(height,  row_number, -1):
        print(" ", end="")


def print_hashes(row_number):
    for i in range(0, row_number):
        print("#", end="")


if __name__ == "__main__":
    main()
