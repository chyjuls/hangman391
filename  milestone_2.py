import random
''' imports the random module which contains a variety of things to do with random number generation.'''

def Choice():
    word_list =['mango','orange','banana','apple','grapes']  #print(word_list)
    random.choice(word_list)
    word = random.choice(word_list)
    return word


'''Create a function that will take in a word and display the number of letters in the word with underscores. '''
def display_word(word):
    word_length = len(word)
    print(word_length)
    for i in range(word_length):
        print("_",end=" ")
    print("\n")

guess = input("Enter a single letter: ")
#print(guess)

# Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.

if len(guess) == 1 and guess.isalpha():
    print("Good guess")
else:
    print("Oops! That is not a valid input.")