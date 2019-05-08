'''
Main file for laser chess
'''
import pygame
from pieces import Deflector, Laser, Switch

board_size = 900
square_size = board_size/9
pygame.init()
screen = pygame.display.set_mode((board_size,board_size))
board = pygame.Surface((board_size, board_size))
while True:
    screen.fill((255,0,0))
    #board.fill((255,0,0))
    pygame.display.flip()

def print_board(board):
    print("\nBoard")
    for i in board:
        print(i)
'''
object_dict = {}
int = 1
for c in 'ab':
    object_dict[c] = Deflector((0,4*int),1,c,'red')
    object_dict[c].plot_piece(board)
    int += 1

object_dict['a'].rotate(3)
object_dict['b'].rotate(4)

object_dict['a'].move((0,6),board)

object_dict['c'] = Deflector((3,4),1,'c')
object_dict['c'].plot_piece(board)

object_dict['L'] = Laser('B')
object_dict['L'].plot_piece(board)
print_board(board)
object_dict['L'].shoot_laser(board, object_dict)

print_board(board)
'''

def main():
    # Initialize board as a 2d list
    board = [[' ' for i in range(9)] for j in range(9)]
    # Create object dict
    object_dict = {}
    # Plot pieces
    board, object_dict = set_up_board(board, object_dict)
    object_dict['RL'].shoot_laser(board)
    print_board(board)

def set_up_board(board, object_dict):
    # Initialize and plot pieces
    i = 1
    for p in '12345':
        object_dict['R'+p] = Deflector((0,i),1,'R'+p,'R')
        object_dict['R'+p].plot_piece(board)
        object_dict['B'+p] = Deflector((8,i),1,'B'+p,'B')
        object_dict['B'+p].plot_piece(board)
        i += 1
    # Initialize lasers
    object_dict['RL'] = Laser('R')
    object_dict['RL'].plot_piece(board)
    return board, object_dict
