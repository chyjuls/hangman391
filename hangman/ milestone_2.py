import random
''' imports the random module which contains a variety of things to do with random number generation.'''

word_list =['mango','orange','banana','apple','grapes']
#print(word_list)

random.choice(word_list)
word = random.choice(word_list)

#print(word)
'''random.choice() is a function that chooses a random item from a list, tuple, or string. '''

guess = input("Enter a single letter: ")
#print(guess)

# Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.

if len(guess) == 1 and guess.isalpha():
    print("Good guess")
else:
    print("Oops! That is not a valid input.")