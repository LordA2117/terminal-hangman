import requests
import random

api = 'https://random-word-api.herokuapp.com/'

def get_word():
    word_unformatted = requests.get(f"{api}word").text
    word = word_unformatted.replace('"', '')
    word = word.replace('[', '')
    word = word.replace(']', '')
    return word

def make_blanks(base_word):
    num_revealed = random.randint(1, int(len(base_word)/2))
    blank_string = ['-']*len(base_word)
    indices = list(range(len(base_word)))
    
    for i in range(num_revealed):
        index = random.choice(indices)
        blank_string[index] = base_word[index]
        indices.remove(index)
    
    return ''.join(blank_string)


def modify_blanks(base_word, blanks, guessed_letter):
    blanks = list(blanks)
    i = 0
    while i < len(base_word):
        if guessed_letter == base_word[i]:
            blanks[i] = guessed_letter
        i += 1
    return ''.join(blanks)

