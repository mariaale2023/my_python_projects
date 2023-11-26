import random
import os
from hangman_ascii import HANGMANPICS, TITLE


#added OS compatibility to improve WIN/MAC compatibility
words_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "words.txt")

with open(words_file_path,"r") as words_file:
    # word catalogue in a text file
    # the list included /n, so strip command is more suitable to create a list from the file
    word_list = [word.strip() for word in words_file.readlines()]


def new_word():
    # selects a new word from the catalogue
    return str(random.choice(word_list))

def look(char, word):
    global guessing
    found = False
    for i in range(len(word)):
        if word[i] == char:
            found = True
            guessing = guessing[:i] + char + guessing[i+1:]
    print(guessing)
    return (found)



while True:
    #reset the game to original values
    game_not_over,lives, guessing  = True, 6, ""

    print(TITLE)
    word = new_word()
    guessing = "_" * len(word)
    
    # print(word)
    print (f"\nthe word has {len(word)} Charaters: {' '.join(guessing)}")
    while game_not_over:
        find = input("guess a letter: ").lower()
        # if the length of the word is more than 1 or not a letter, ignore and ask again  
        if len(find) != 1 or not find.isalpha():
            print("Please enter a single alphabetic character.")
            continue
        if not look(find[0], word):
            lives -=1
            print(HANGMANPICS[lives])
        if lives == 0:
            print(f"Game over! The word was '{word}'.")
            game_not_over = False
        elif "_" not in guessing:
            print(f"Congratulations! You guessed the word: '{word}'.")
            game_not_over = False
    exit_prompt = input("to exit the game, enter 'exit': ").lower()
    print(exit_prompt)
    if exit_prompt == "exit":
        break    

print("\nthanks for playing")


