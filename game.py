from player import Player
from board import Board

class TicTacToeGame:

    def start(self):
        print("**************************")
        print("  Welcome to Tic-Tac-Toe  ")
        print("**************************")

        board = Board()
        player = Player()
        computer = Player(False)

        while True:

            board.print_board()

            while True:

                player_move = player.get_move()
                board.submit_move(player, player_move)
                board.print_board()

                if board.check_is_game_over(player, player_move):
                    print("Awesome. You won the game!")
                    break
                elif board.check_is_tie():
                    print("It's a tie! Try again.")
                    break
                else:
                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()

                    if board.check_is_game_over(computer, computer_move):
                        print("Oops... The computer won. Try again.")
                        break
                    elif board.check_is_tie():
                        print("It's a tie! Try again.")
                        break
            play_again = input("Would you like to play again? Enter X for YES or O for NO: ")

            if play_again == "O":
                print("Bye! Come back soon")
                break
            elif play_again == "X":
                self.start_new_round(board)
            else:
                print("Your input was not valid but I will assume that you want to play again.")
                self.start_new_round(board)

    def start_new_round(self, board):
        print("*************")
        print("  New Round  ")
        print("*************")

        board.reset_board()
        board.print_board()

game = TicTacToeGame()
game.start()