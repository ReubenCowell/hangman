# Reuben Cowell
# This is my GCSE NEA project submission: Hangman

import json # json is used to store my word list
import random # random is used to pick a random word from the json file


def get_word():
    in_word = ""
    while len(in_word) < 3 or len(in_word) > 10:
        with open('wordlist.json', 'r') as f:
            in_word = random.choice(json.load(f))
        f.close()
    return in_word, len(in_word)


word, len_word = get_word()

print(word, len_word)