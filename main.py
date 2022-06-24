import random
import string

from words import data


def hangman():
    word = random.choice(data)
    word_letters = set(word)  # selected word letters
    used_letters = set()  # previously guessed letters
    alphabets = set(string.ascii_lowercase)
    while len(word_letters) > 0:
        all_letters = [letter if letter in used_letters else '-' for letter in word]
        print(' '.join(all_letters))
        print(f"Guessed letters are {used_letters} ")
        guessed_letter = input("Enter a letter: ")  # letter entered by user

        if guessed_letter in alphabets - used_letters:
            used_letters.add(guessed_letter)
            if guessed_letter in word_letters:
                word_letters.remove(guessed_letter)
                print("You guessed a correct letter !")
        elif guessed_letter in used_letters:
            print("you have already guessed that letter !")
        else:
            print("Invalid character !")
    print("YAY ! You guessed the word !")


hangman()
