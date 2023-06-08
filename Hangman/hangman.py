import random
import string

from words import words


def get_valid_word(words_list):
    word = random.choice(words_list)
    while '-' in word or ' ' in word:
        word = random.choice(words_list)
    return word


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabets = set(string.ascii_lowercase)
    used_letters = set()
    lives = 7

    # Get input from the user
    while len(word_letters) > 0 and lives > 0:
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print("You have ", lives, " lives left and you used these letters: ", ' '.join(used_letters))

        letters_guessed = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(letters_guessed))

        user_letter = input('Guess a letter: ')  # what the user has guessed
        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1  # wrong guess take away a life
                print("Guessed letter not in word")

        elif user_letter in used_letters:
            print("You have already used that character. Please try again")

        else:
            print("Invalid character. Please try again")

    # Gets here when word_letters is zero
    if lives == 0:
        print("You died, sorry. The word was ", word)
    else:
        print("You have guessed the word correctly, ", word, " !!")


hangman()
