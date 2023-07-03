import os
from pictures import HANGMANPICS
from get_words import get_word, make_blanks, modify_blanks
from termcolor import colored
from time import sleep

word = get_word()
num_guess = len(HANGMANPICS) # Number of guesses of the user

num_rows = len(word)

colours = ['green', 'cyan', 'yellow', 'magenta', 'white', 'light_red', 'red']

print(colored('Hangman is a game of guessing', 'green'))
print(colored('Your goal is to guess the word and save the man from certain death', 'yellow'))
print(colored('Can you save him on time \U0001F608 ? ', 'red'))
sleep(3)
os.system('cls')

i = 0
blanks = make_blanks(word)
guessed_letter = None
available_letters = list(word)
# Main game loop
while i != num_guess - 1:
    

    print(colored(HANGMANPICS[i], colours[i]))
   

    if not guessed_letter:
        print(blanks)
   
    if guessed_letter:
        blanks = modify_blanks(word, blanks, guessed_letter)
        print(blanks)
        if blanks == word:
            os.system('cls')
            print(colored('You win \U0001F3C6!', 'cyan'))
            break

    guessed_letter = input('Guess the letter: ')
    
    if guessed_letter not in word:
        i += 1
    
    if guessed_letter in word and guessed_letter not in available_letters:
        i += 1

    if guessed_letter in word and guessed_letter in available_letters:
        for letter in available_letters:
            if letter == guessed_letter:
                available_letters.remove(letter)


    os.system('cls')
else:
    print(colored(HANGMANPICS[-1], colours[-1]))
    print(f'The word was {word}')
#TODO: Finish the game
