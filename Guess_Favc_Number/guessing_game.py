import random


def user_guess_game(fav_no):
    random_number = random.randint(1, fav_no)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {fav_no} : "))
        if guess < random_number:
            print("Sorry, Guess again. Too low.")
        elif guess > random_number:
            print("Sorry, Guess again. Too High.")

    print(
        f"Just Right, Congratulations ! You have guessed the random number {random_number} correctly.")


def computer_guess_game(upper_cutoff):
    low = 1
    high = upper_cutoff
    feedback = ""
    while feedback != 'c':
        if low != high:
            guessed_number = random.randint(low, high)
        else:
            guessed_number = low  # Could also assign high
        feedback = input(f"Is the {guessed_number} too High (H), \
                         too low (L), or correct (C)").lower()
        if feedback == 'h':
            high = guessed_number - 1
        elif feedback == 'l':
            low = guessed_number + 1

    print(
        f" Hurray, The computer guessed your number, {guessed_number}, correctly!")


# Get user's favorite number
fav_number = int(input("Enter your favorite number : "))
option = int(input("Enter any one of the options, \
1. User guessing game (1) \
2. Computer guessing game (2) "))

match option:
    case 1:
        user_guess_game(fav_number)
    case 2:
        computer_guess_game(fav_number)
