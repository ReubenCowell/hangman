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


print("Welcome to Hangman, created by Reuben Cowell")
ready = input("Are you ready to play? (y/n) >>> ")

while ready == "y":
	lives = 6
	bad_guesses = []
	unguessed_list = ["_"]
	word, len_word, char_list = get_word()
	#print(word, len_word, char_list)
	print("You have " + str(lives) + " lives!")
	unguessed_list = unguessed_list * len_word
	print(" ".join(unguessed_list))
		

	ready = input("Do you still want to play? (y/n) >>> ")
print("bye then")
