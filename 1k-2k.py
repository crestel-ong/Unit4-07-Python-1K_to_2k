#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Sept 2021
# This 1k to 2k program


def main():
    # This function has about nested loops
    # it prints out the numbers in the range, 5 #s per line

    # process and output
    for counter in range(1000, 2001):  # prints out numbers from 1000 to 2000
        if (counter + 1) % 5 == 0:  # +1 because if not 1st line is just 1000
            print("{0}".format(counter), "")  # start new line bcuz no end=""
        else:  # without the "" the #s have no space between
            print("{0}".format(counter), "", end="")  # end="" continues
            #   printing on same line

    print("")
    print("\nDone.")


if __name__ == "__main__":
    main()
