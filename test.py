from hangman_words import word_list
import random

word = random.choice(word_list).lower()
hidden_word = len(word) * "_"
guess_letter = input("Guess letter: ")

for i, letter in enumerate(word):
    if letter != "_" and guess_letter == letter:
        hidden_wordword[i] = letter
print("".join(hidden_word))
