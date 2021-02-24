from hangman_words import word_list
import random

word = random.choice(word_list).lower()
secret_word = len(word) * "_"
hidden_word = len(word) * ["_"]


def hangman():
    print(f"There are {len(word)} letters in {secret_word}")
    letters = []
    tries = 5

    while tries != 0:
        guess_letter = input("Guess a letter: ")
        if guess_letter in word:
            print(f"You guessed right, you have {tries} tries left")

        else:
            print(f"You guess wrong, you have {tries} tries left")
            tries -= 1

        if guess_letter in letters:
            letters += guess_letter
        else:
            letters += guess_letter

        for i, letter in enumerate(word):
            if letter != "_" and guess_letter == letter:
                hidden_word[i] = letter
        print("".join(hidden_word))
        print(letters)

    print(f"You lost, the right word was {word}")

hangman()


############
# def hangman():
#     print(f"There are {len(word)} letters in {secret_word}")
#     letters = {}
#     tries = 5
#
#     while tries != 0:
#         guess_letter = input("Guess a letter: ")
#         if guess_letter in word:
#             print(f"You guessed right, you have {tries} tries left")
#
#         else:
#             print(f"You guess wrong, you have {tries} tries left")
#             tries -= 1
#
#     print(f"You lost, the right word was {word}")
#
# def show_dict():
#     if guess_letter in letters:
#         letters[guess_letter] += 1
#     else:
#         letters[guess_letter] = 1
#
#
# def show_letters():
#     for i, letter in enumerate(word):
#         if letter != "_" and guess_letter == letter:
#             hidden_word[i] = letter
#     print("".join(hidden_word))
#     print(letters)
#
# def game():
#     hangman()
#     show_dict()
#     show_letters()
#