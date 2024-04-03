import random
import os
# Clears import messages. Same code used later to clear all previous steps.
os.system('cls' if os.name == 'nt' else 'clear')
# Variables to store ascii arts, are drawn later by func play_hangman
hangman = '''
  +---+
  |   |
      |
      |
      |
      |
========='''
hangman2 = '''
  +---+
  |   |
  O   |
      |
      |
      |
========='''
hangman3 = '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========='''
hangman4 = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========='''
hangman5 = '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''' 
hangman6 = '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=======
==''' 

hangman7 = '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''

hangman8 = '''
  +---+
  -   |
  O   |
 /|\o |
 / \  |
      |
========='''

hangman9 = '''
  +---+
  |   |
  O   |
o/|\o |
 / \  |
      |
========='''



# Function that is called later under "play_hangman." Returns a user input to decide the mode.
def choose_mode():
    print('Do you want a random word, or to choose a word?')
    print('Type "1" for random or "2" for choose.')
    return input('choose mode: ')
# Returns a string from the user for mode type "choose"    
def choose_word():
    return input('type a word: ').lower()

# Function to print the hangman board. Works by finding the number of letters in rand or input word, and writes a "_" for each.
# Function later checks to see if user has correctly guessed any letters by checking contents of "guessed_letters" and if they match any in "display_word"
def print_board(word, guessed_letters):
    display_word = ""
    for letter in word:
        if letter == ' ':
            display_word += "  "  # Always display spaces
        elif letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word)

# Function to check if the word has been guessed. Goes by letter in "word" and checks if it is contained in list "guessed_letters"
def is_word_guessed(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True
# Function to play the game. First if checks if user selected mode random. If true, chooses random word for use by assigning random word from list "book_words" to variable "word"

def play_hangman():
    mode_set = int(choose_mode())  
    if mode_set == 1:
        book_words = ["dog", "cat", "house", "tree", "river", "mountain", "ocean", "sun", "moon", "star"]
        word = random.choice(book_words)
    elif mode_set == 2:
        word = choose_word()
        os.system('cls' if os.name == 'nt' else 'clear')

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Incorrect Input')
        return  # Exit the function if the input is incorrect

    guessed_letters = []
    hangman_parts = 0

    print("Welcome to Hangman!")
    print("Try to guess the word.")
    while hangman_parts < 9:
        print_board(word, guessed_letters)
        if hangman_parts == 1:
            print(hangman)
        if hangman_parts == 2:
            print(hangman2)
        if hangman_parts == 3:
            print(hangman3)
        if hangman_parts == 4:
            print(hangman4)
        if hangman_parts == 5:
            print(hangman5)
        if hangman_parts == 6:
            print(hangman6)
        if hangman_parts == 7:
            print(hangman7)
        if hangman_parts == 8:
            print(hangman8)
        if hangman_parts == 9:
            print(hangman9)
      
        guess = input("Guess a letter or the whole phrase: ").lower()
        if len(guess) == 1:
            if guess in guessed_letters:
                os.system('cls' if os.name == 'nt' else 'clear')
                print ('Already Guessed!')
                hangman_parts += 1
            elif guess in word:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Correct guess!")
                guessed_letters.append(guess)
                if is_word_guessed(word, guessed_letters):
                    print_board(word, guessed_letters)
                    print("Congratulations! You guessed the word:", word)
                    return
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Incorrect guess!")
                hangman_parts += 1
        elif len(guess) > 1:
            if guess == word:
                print("Congratulations! You guessed the word:", word)
                return
            else:
                print("Incorrect guess!")
                hangman_parts += 1
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Sorry, you lost. The word was:", word)
    print(hangman9)
# Start the game
play_hangman()
