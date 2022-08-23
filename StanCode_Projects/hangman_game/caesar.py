"""
File: caesar.py
Name:
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    find the new alphabet firstly then use a function to decipher the input to origin alphabet
    """
    n = int(input('Secret number: '))
    x = ALPHABET[len(ALPHABET)-n:]  # know where the new alphabet start from
    s = x + ALPHABET[:len(ALPHABET) - n]  # new alphabet
    e = input("What's the ciphered string? ")
    e = e.upper()  # case-insensitive
    ans = replace(e, s)  # decipher function
    print('THe deciphered string is: '+str(ans))


def replace(e, s):
    ans = ''
    for i in range(len(e)):
        if e[i].isalpha():
            pos = s.find(e[i])  # find the each position of input to correspond origin alphabet
            ans += ALPHABET[pos]
        else:  # the input content except from alphabet
            ans += e[i]
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
