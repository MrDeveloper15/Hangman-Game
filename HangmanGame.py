import random

word_list = ['python', 'java', 'kotlin', 'javascript']
hangman_pics = ['''
  +---+
  O   |
      |
      |
      |
      |
=========
''', ''' (more stages here) ''']

def display_hangman(tries):
    return hangman_pics[tries]

def get_word():
    return random.choice(word_list).upper()

def play():
    word = get_word()
    guessed_letters = []
    tries = 6
    guessed_word = ['_' for _ in word]
    
    while tries > 0 and ''.join(guessed_word) != word:
        print(display_hangman(tries))
        print(" ".join(guessed_word))
        
        guess = input("Guess a letter: ").upper()
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            guessed_word = [letter if letter == guess else guessed_word[i] for i, letter in enumerate(word)]
        else:
            guessed_letters.append(guess)
            tries -= 1
    
    if ''.join(guessed_word) == word:
        print("Congratulations, you won!")
    else:
        print(f"Sorry, you lost! The word was {word}.")

play()
