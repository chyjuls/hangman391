import random


 
'''This class represents a game of Hangman.'''
''' It takes a list of words as an input and randomly selects one of them as the word to be guessed.'''
'''The user can guess letters until they either win or lose.'''
'''The user can also choose the number of lives they want to have.'''

class Hangman:

   
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []
    
# This method checks if the guessed letter is in the word and updates the word_guessed list accordingly.


    def check_guess(self, guess):
        guess = guess.lower()
        self.list_of_guesses.append(guess)

        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for i in range(len(self.word)):
                if self.word[i]==guess:
                    self.word_guessed[i] = guess
                if '_' not in self.word_guessed:
                    print(f"Congratulations! You've guessed the word: {''.join(self.word_guessed)}")
                    return True    
            self.num_letters -= 1
        else: 
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')
        if self.num_lives <= 0:
                print(f"Game over! The word was: {self.word}")
                return True
             # code when the number of lives is 0, fixing a bug...




    def ask_for_input(self):
        while True:
            guess = input('Guess a letter: ')
            guess = guess.lower()
            if len(guess) != 1 or not guess.isalpha():
                print('Invalid input. Please enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already guessed that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

'''This function takes a list of words as an input and starts a game of Hangman.'''



def play_game(word_list):
        num_lives = 5
        game = Hangman(word_list, num_lives)
        while True:
            if game.num_lives == 0:
                print(f'You lost!')
                break
            elif game.num_letters > 0:
                game.ask_for_input()
            else:
                print(f'Congratulations! You\'ve guessed the word: {game.word}')

                break
            
'''This function takes a list of words as an input and starts a game of Hangman.'''

      # Define your word list

word_list = ['mango', 'orange', 'banana', 'apple', 'grapes']
play_game(word_list)

  
  
                   