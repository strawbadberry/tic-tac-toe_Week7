from logic import TicTacToe

def print_board(board):
    for i, row in enumerate(board):
        print(' | '.join(cell if cell is not None else ' ' for cell in row))
        if i < 2:
            print('---+---+---')

def main():
    mode = input("Choose mode (1 for single player, 2 for two players): ")
    game = TicTacToe(mode)
    
    while True:
        print_board(game.board)
        game.play_turn()
        winner = game.get_winner()
        
        if winner:
            print_board(game.board)
            print(f"Player {winner} wins!")
            break
            
        if game.is_draw():
            print_board(game.board)
            print("It's a draw!")
            break

if __name__ == '__main__':
    main()
