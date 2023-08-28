# Reuben Cowell
# This is my GCSE NEA project submission: Hangman

import json # json is used to store my word list
import random # random is used to pick a random word from the json file


with open('wordlist1.json', 'r') as f:
    word = " "
    while len(word) < 3 or len(word) > 10:
        print(word)
        word = random.choice(json.load(f))
f.close()

print(word, len(word))