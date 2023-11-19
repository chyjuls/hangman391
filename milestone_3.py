import random

# imports the random module which contains a variety of things to do with random number generation.
word = random.choice(['mango','orange','banana','apple','grapes'])  #print(word_list)

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else: 
        print(f'Sorry, {guess} is not in the word.')

''' Defines function that checks if the guessed letter is in the word.'''

def ask_for_input():
    while True:
        guess = input("Please guess a letter: ")
        if guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

''' Defines function that asks the user to guess a letter and checks if the input is valid.'''

# Call the function to start the game
ask_for_input()
