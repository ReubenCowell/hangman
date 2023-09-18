# Reuben Cowell
# This is my GCSE NEA project submission: Hangman

import json  # json is used to store my word list
import random  # random is used to pick a random word from the json file


def get_word():
	# this function will get a random word from the word list and returns the word, the length of the word and the word as a list of characters
	in_word = ""
	while len(in_word) < 3 or len(in_word) > 10:
		with open('wordlist.json', 'r') as f:
			in_word = random.choice(json.load(f))
		f.close()
	return in_word, len(in_word), list(in_word)


def get_guess(): # This is used to get a single letter guess from a user, and will keep trying to get a guess until it is 'legal'
	initial_guess = input("Please enter your guess >>> ")
	while len(initial_guess) > 1 or initial_guess.isalpha() == False:
		initial_guess = input("Guess must be a singular letter >>> ")
	return initial_guess


def status_update(): # this prints to the screen a user's current lives and their bad guesses
	print("----------\nLives: " + str(lives) + "\nBad guesses: " +
	      ", ".join(bad_guesses) + "\nCurrent word: " + " ".join(unguessed_list))


print("Welcome to Hangman, created by Reuben Cowell")
ready = input("Are you ready to play? (y/n) >>> ")

while ready == "y":
	lives = 6  # reset lives at the start of the game
	bad_guesses = []  # resets a list of bad guessed lessons
	word, len_word, char_list = get_word()  # this runs the guess word function
	unguessed_list = ["_"] * len_word  # this sets up a list of underscores
	progress = 0 # a counter that shows how many letters in a word have been counted - wil be compared against word len
	won = False
	# print(word, len_word, char_list)

	print("\n---------------------- \nYou have " + str(lives) + " lives!")
	print("Current word: " + " ".join(unguessed_list))

	while lives > 0 and won == False:
		guess = get_guess()
		if guess in bad_guesses: # if the guess has been already guessed by user, it asks the user to guess again
			print('Already guessed: \n' + ", ".join(bad_guesses) + '\n')
		elif char_list.count(guess) == 0: # if the guess is incorrect, it will take a life and add the bad guess to a bad word list
			print("Unlucky, guess not in word.\nLife lost\n")
			bad_guesses.append(guess)  # adds the incrrect guess to the list of bad guesses
			lives -= 1
			status_update() # prints the progress to the screen
		elif guess in char_list:
			if char_list.count(guess) > 1: # TODO handle what happens when there 
				print('The letter you guess')
				num_in_word = char_list.count(guess)
				for i in range(num_in_word):
					guess_loc = char_list.index(guess)
					unguessed_list[guess_loc] = guess
					char_list[guess_loc] = '_'
					progress += 1
				print('Congratulations, you got ' + str(num_in_word) + ' letters!')
				status_update()
			else:
				guess_loc = char_list.index(guess)
				unguessed_list[guess_loc] = guess 
				print("\nCorrect! Letter in word!\n")
				status_update()
				progress += 1
				if progress == len_word:
					print('CONGRATULATIONS! \nYou won, the word was: '+word)
					won = True
		if lives == 0:
			print("GAME OVER! \nThe word was: "+word)

	ready = input("\nDo you want to play again (y/n) >>> ")

print("bye then")


# TODO: tidy up what is printed to the user
# TODO: test program 