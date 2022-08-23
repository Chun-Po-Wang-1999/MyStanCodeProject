"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    a function that can check your input alphabet if fits the random word.
    """
    ran = random_word()
    dash = ''
    for i in range(len(ran)):  # detect how many words does random_word have.
        dash += '-'
    n = N_TURNS
    print('The word looks like '+str(dash))
    print('You have '+str(n)+' wrong guesses left.')
    ans = dash  # for the word rearranged purpose.
    while True:
        alpha_guess = input('Your guess:')
        if not alpha_guess.isalpha():  # preclude Punctuation.
            print('Illegal format.')
        else:
            upper_guess = alpha_guess.upper()  # let the function become case-insensitive.
            if ran.find(upper_guess) == -1:  # wrong guess, can't find the input alphabet in random word.
                n -= 1
                print('There is no '+str(upper_guess)+'\'s in the word')
                if n == 0:  # you don't have any life.
                    print('You are completely hung :(')
                    print('The word was: ' + str(ran))
                    break
                print('The word looks like ' + str(ans))
                print('You have '+str(n)+' wrong guesses left.')
            else:  # right guess.
                pos = ran.find(upper_guess)  # find the position of guessed alphabet in random word.
                ans = ans[:pos]+upper_guess+ans[pos+1:]  # rearrange the answer by plug in right guessed alphabet.
                if ran[pos+1:].find(upper_guess) != -1:
                    # find the second position of same guessed alphabet, if necessary.
                    pos1 = ran[pos+1:].find(upper_guess)
                    ans = ans[:pos + pos1 + 1] + upper_guess + ans[pos + pos1 + 2:]
                    if ran[pos+pos1 + 2:].find(upper_guess) != -1:
                        # find the third position of same guessed alphabet, if necessary.
                        pos2 = ran[pos+pos1 + 2:].find(upper_guess)
                        ans = ans[:pos + pos1 + pos2 + 2] + upper_guess + ans[pos + pos1 + pos2 + 2:]
                print('Yoy are correct!')
                if ans == ran:  # finish all guessing and you got the right answer.
                    print('You win!!')
                    print('The word was: '+str(ran))
                    break
                print('The word looks like ' + str(ans))
                print('You have ' + str(n) + ' wrong guesses left.')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
