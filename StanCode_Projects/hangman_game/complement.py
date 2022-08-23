"""
File: complement.py
Name: Louis
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    the user can input a DNA string regardless of the case
    then the program will output a correspond answer
    """
    DNA = input("Please give me a DNA strand and I'll find the complement: ")
    ans = build_complement(DNA)
    print('The complement of '+str(DNA)+' is '+str(ans))


def build_complement(DNA):
    """
    Capitalize all alphabet firstly, then change the upper alphabet to their correspond alphabet
    by starting with another empty string(ans1)
    then return ans
    """
    ans = ''  # empty string
    for i in range(len(DNA)):
        ch = DNA[i]
        if ch.islower():
            ans += ch.upper()
        else:
            ans += ch
    ans1 = ''  # Another empty string
    for i in range(len(ans)):
        ch = ans[i]
        if ch == 'A':
            ans1 += 'T'
        if ch == 'T':
            ans1 += 'A'
        if ch == 'C':
            ans1 += 'G'
        if ch == 'G':
            ans1 += 'C'
    ans = ans1  # assign the finished string to ans
    return ans

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
