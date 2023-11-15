import random

class TicTacToe:
    def __init__(self, mode):
        self.board = [[None] * 3 for _ in range(3)]
        self.players = ['X', 'O']
        self.current_player = self.players[0]
        self.other_player = self.players[1] if mode == '1' else self.players[0]

    def play_turn(self):
        x, y = self.get_move()
        self.board[x][y] = self.current_player
        self.current_player, self.other_player = self.other_player, self.current_player

    def get_winner(self):
        for i in range(3):
            if all(self.board[i][j] == self.board[i][0] for j in range(3)) and self.board[i][0] is not None:
                return self.board[i][0]
            if all(self.board[j][i] == self.board[0][i] for j in range(3)) and self.board[0][i] is not None:
                return self.board[0][i]

        if all(self.board[i][i] == self.board[0][0] for i in range(3)) and self.board[0][0] is not None:
            return self.board[0][0]
        if all(self.board[i][2 - i] == self.board[0][2] for i in range(3)) and self.board[0][2] is not None:
            return self.board[0][2]

        return None

    def is_draw(self):
        return all(all(cell is not None for cell in row) for row in self.board)

    def get_move(self):
        if self.current_player == 'X':
            return map(int, input(f"Enter the position of (x,y) for {self.current_player}, split with comma: ").split(","))
        else:
            empty_spots = [(x, y) for x in range(3) for y in range(3) if self.board[x][y] is None]
            return random.choice(empty_spots) if empty_spots else (0, 0)