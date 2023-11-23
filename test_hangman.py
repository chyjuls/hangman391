
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        self.list_of_guesses.append(guess)

        if guess in self.word:
            print(f'Good guess! "{guess}" is in the word.')
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            if '_' not in self.word_guessed:
                print(f"Congratulations! You've guessed the word: {''.join(self.word_guessed)}")
                return True
        else:
            self.num_lives -= 1
            print(f'Sorry, "{guess}" is not in the word.')
            if self.num_lives <= 0:
                print(f"Game over! The word was: {self.word}")
                return True
            else:
                print(f'You have {self.num_lives} lives left.')
        return False
            
    def ask_for_input(self):
        while True:
            print(f"Current word: {' '.join(self.word_guessed)}")
            guess = input('Guess a letter: ').strip()
            if not guess.isalpha() or len(guess) != 1:
                print('Invalid input. Please, enter a single alphabetical character.')
                continue
            if guess.lower() in self.list_of_guesses:
                print('You already guessed that letter!')
                continue
            if self.check_guess(guess):
                break

# Define your word list
word_list = ['mango', 'orange', 'banana', 'apple', 'grapes']

# Create an instance of the Hangman class
game = Hangman(word_list)
game.ask_for_input()


