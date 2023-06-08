import math
import random


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid spot for the next move
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            # we're going to check that this is a correct value by trying to
            # cast it to an integer, and if it's not, then we say its invalid
            # if that spot is not available on the board, we say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True  # if successful
            except ValueError:
                print('Invalid square, Try again.')

        return val


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        valid_moves = game.available_moves()
        if len(valid_moves) == 9:
            square = random.choice(valid_moves)  # randomly choose one move

        else:
            # get the square based off the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    # recursive algorithm
    def minimax(self, state, player):
        max_player = self.letter  # the current player
        other_player = 'O' if player == 'X' else 'X'

        # First, we want to check if the prev move is a winner
        # this is our base case
        if state.current_winner == other_player:
            # Dictionary with position and utility function score
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player
                    else -1 * (state.num_empty_squares() + 1)}

        elif not state.empty_squares():  # no empty squares
            return {'position': None, 'score': 0}

        # initialize the dictionaries
        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize (be larger)
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize

        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)

            # step 2: recurse using minimax to simulate the game after making the move
            sim_score = self.minimax(state, other_player)  # now alternate the players

            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            # step 4: update the dictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:  # if greater score best for current player
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:  # lower score best for other player / minimize
                    best = sim_score

        return best
