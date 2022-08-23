"""
File: rocket.py
Name:Louis
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    divide the rocket into 4 parts, and 2 parts are same
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    """
    divide into 3 for loop: space, /, \
    """
    for i in range(SIZE):  # /\
        for j in range(SIZE-i):
            print(' ', end='')
        for j in range(i+1):
            print('/', end='')
        for j in range(i+1):
            print("\\", end='')
        print('')


def belt():
    """
    divide into 3 for loop: +, =, +
    """
    for i in range(1):
        for j in range(1):
            print('+', end='')
        for j in range(SIZE*2):  # bilateral symmetry
            print('=', end='')
        for j in range(1):
            print('+', end='')
        print('')


def upper():
    """
    divide into 5 for loop: |, ., /\, ., |
    """
    for i in range(SIZE):
        for j in range(1):
            print('|', end='')
        for j in range(SIZE-i-1):
            print('.', end='')
        for j in range((i+1)*2):  # /\ use if/else to distinguish even/odd, presenting different patterns
            if i % 2 == 0:  # i is even
                if (i+j) % 2 == 0:  # (i+j) is even
                    print('/', end='')
                else:
                    print("\\", end='')
            if i % 2 == 1:  # i is odd
                if (i+j) % 2 == 1:  # (i+j) is odd
                    print('/', end='')
                else:
                    print("\\", end='')
        for j in range(SIZE-i-1):
            print('.', end='')
        for j in range(1):
            print('|', end='')
        print('')


def lower():
    """
    Symmetrical up and down of upper()
    """
    for i in range(SIZE):
        for j in range(1):
            print('|', end='')
        for j in range(i):
            print('.', end='')
        for j in range(SIZE*2-2*i):  # \/
            if i % 2 == 0:  # i is even
                if (i+j) % 2 == 0:  # (i+j) is even
                    print("\\", end='')
                else:
                    print('/', end='')
            if i % 2 == 1:  # i is odd
                if (i+j) % 2 == 1:  # (i+j) is odd
                    print("\\", end='')
                else:
                    print('/', end='')
        for j in range(i):
            print('.', end='')
        for j in range(1):
            print('|', end='')
        print('')
# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
