import random
import string
from words import data


def hangman():
    word = random.choice(data)
    word_letters = set(word)  # selected word letters
    used_letters = set()  # previously guessed letters
    alphabets = set(string.ascii_lowercase)
    lives = 7
    while len(word_letters) > 0 and lives > 0:
        all_letters = [letter if letter in used_letters else '-' for letter in word]
        print(' '.join(all_letters))
        print(f"You have used {lives} lives and guessed letters are {used_letters} ")
        guessed_letter = input("Enter a letter: ")  # letter entered by user

        if guessed_letter in alphabets - used_letters:
            used_letters.add(guessed_letter)
            if guessed_letter in word_letters:
                word_letters.remove(guessed_letter)
                print("You guessed a correct letter !")
            else:
                lives = lives - 1

        elif guessed_letter in used_letters:
            print("you have already guessed that letter !")
        else:
            print("Invalid character !")

    if lives == 0:
        print(f"You lost! The correct answer was {word}.")
    else:
        print(f"YAY ! You guessed the word {word} !")


hangman()
