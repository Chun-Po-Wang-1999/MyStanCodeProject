"""
File: anagram.py
Name: Louis
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    start = time.time()
    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################
    print("Welcome to stancode \"Anagram Generator\"(or -1 to quit)")
    while True:
        answer = input('Find anagrams for: ')
        if answer == EXIT:
            break
        find_anagrams(answer)
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    dictionary_list = []
    with open(FILE, 'r') as f:
        for line in f:
            dictionary_list.extend(line.split())
    return dictionary_list


def find_anagrams(s):
    """
    :param s:
    :return:
    """

    dictionary_list = read_dictionary()
    refined_dictionary_list = []
    for i in range(len(dictionary_list)):
        if len(dictionary_list[i]) == len(s):
            refined_dictionary_list.append(dictionary_list[i])
    anagrams = []
    find_anagrams_helper(s, anagrams, '', refined_dictionary_list)
    print(f"{len(anagrams)} anagrams: {anagrams}")


def find_anagrams_helper(s, anagrams, vocab, dictionary_list):
    if len(s) == 0:  # base case
        if vocab not in anagrams:
            print('Searching...')
            print('Found: ', vocab)
            anagrams.append(vocab)
    else:
        for i in range(len(s)):  # non-dynamic
            # choose
            vocab += s[i]
            new_s = s[:i]+s[i+1:]
            if has_prefix(vocab, dictionary_list):
                # explore
                find_anagrams_helper(new_s, anagrams, vocab, dictionary_list)
            # un-choose
            vocab = vocab[0:len(vocab)-1]


def has_prefix(sub_s, dictionary_list):
    """
    :param dictionary_list:
    :param sub_s:
    :return: booing
    """
    for word in dictionary_list:
        if word.startswith(sub_s):
            return True
    return False



if __name__ == '__main__':
    main()
