'''
Main file for laser chess
'''
from pieces import Deflector, Laser, Switch

# Initialize board
board = [[' ' for i in range(9)] for j in range(9)]

def print_board(board):
    print("\nBoard")
    for i in board:
        print(i)

object_dict = {}
int = 1
for c in 'ab':
    object_dict[c] = Deflector((0,4*int),1,c)
    object_dict[c].plot_piece(board)
    int += 1

object_dict['a'].rotate(3)
object_dict['b'].rotate(4)

object_dict['c'] = Deflector((3,4),1,'c')
object_dict['c'].plot_piece(board)

object_dict['L'] = Laser('B')
object_dict['L'].plot_piece(board)
print_board(board)
object_dict['L'].shoot_laser(board, object_dict)

print_board(board)
