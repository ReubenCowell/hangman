# Reuben Cowell
# This is my GCSE NEA project submission: Hangman

import json  # json is used to store my word list
import random  # random is used to pick a random word from the json file


def get_word():
	in_word = ""
	while len(in_word) < 3 or len(in_word) > 10:
		with open('wordlist.json', 'r') as f:
			in_word = random.choice(json.load(f))
		f.close()
	return in_word, len(in_word), list(in_word)

def get_guess():
    initial_guess = input("Please enter your guess >>> ")
    while len(initial_guess) > 1 or initial_guess.isalpha() == False:
            initial_guess = input("Guess must be a singular letter >>> ")
    return initial_guess

def status_update():
    print("----------\nLives: " + str(lives) + "\nBad guesses: " + ", ".join(bad_guesses) + "\nCurrent word: " + " ".join(unguessed_list))


print("Welcome to Hangman, created by Reuben Cowell")
ready = input("Are you ready to play? (y/n) >>> ")

while ready == "y":
    lives = 6
    bad_guesses = []
    word, len_word, char_list = get_word()
    unguessed_list = ["_"] * len_word
    print(word, len_word, char_list)

    print("\n---------------------- \nYou have " + str(lives) + " lives!")
    print("Current word: " + " ".join(unguessed_list))

    while lives > 0:
        guess = get_guess()
        if char_list.count(guess) == 0:
            print("Unlucky, guess not in word.\nLife lost")
            bad_guesses.append(guess)
            lives -= 1
            status_update()
        #elif char_list.count(guess) == 1:
        #    print("Correct! Letter in word!")



    ready = input("Good game \nDo you want to play again (y/n) >>> ")

print("bye then")
