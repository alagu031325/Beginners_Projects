import random


# r > s , s > p, p > r
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


def play():
    user = input("What's your choice, 'r' for rock, 'p' for paper, 's' for scissors : ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return f"The opponent's choice is {computer}, It's a tie"

    if is_win(user, computer):
        return f"The opponent's choice is {computer}, You won!"

    return f"The opponent's choice is {computer}, You lost!"


play_game = 'y'
while play_game == 'y':
    print(play())
    play_game = input("Do you want to continue playing? Type (Y) for yes and (N) for no").lower()

print("Bye! Thanks for Playing")
