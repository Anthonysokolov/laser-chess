'''
Main file for laser chess
'''
import pygame
import json
import time
from pieces import Deflector, Laser

# Load board setups
with open('setups.json') as f:
    setups = json.load(f)

# Set board and square size
tiles = 9
square_size = 100
board_size = tiles * square_size

# Initialize pygame and load piece images
pygame.init()
screen = pygame.display.set_mode((board_size,board_size))
rtriangle = pygame.image.load("rtriangle.png").convert_alpha()
rotated = pygame.transform.rotate(rtriangle, 90)

# Create a 2d list to represent the board
board = [[' ' for i in range(9)] for j in range(9)]

rdef_locs = []
rdef_angles = []
bdef_locs = []
bdef_angles = []
comp = tiles - 1

for i in setups['ace']['red_deflectors'].values():
    i = [int(j) for j in i.split()]
    r = i[0]
    c = i[1]
    angle = i[2]

    rdef_locs.append((r,c))
    rdef_angles.append(angle)
    # Have blue pieces mirror the reds
    bdef_locs.append((comp - r, comp - c))
    bdef_angles.append((angle + 2) % 4)

for i in range(len(rdef_locs)):
    # COMBINE WITH ABOVE LOOP
    rloc = rdef_locs[i]
    bloc = bdef_locs[i]

    board[rloc[0]][rloc[1]] = Deflector(rloc,rdef_angles[i],'red',square_size)
    board[bloc[0]][bloc[1]] = Deflector(bloc,bdef_angles[i],'blue',square_size)

board[0][0] = Laser(1,'red', square_size)
board[8][8] = Laser(1,'blue', square_size)

def translate_board(board):
    for row in board:
        for pos in row:
            if pos != ' ':
                pos.display(screen)


def print_board(board):
    print("\nBoard")
    for i in board:
        print(i)

def valid_coords(piece, coords):
    if piece.row == coords[0] and piece.col == coords[1]:
        return False
    if abs(piece.row - coords[0]) <= 1 and abs(piece.col - coords[1]) <= 1:
        return True
    return False

def new_color(color):
    if color == 'blue':
        return 'red'
    else:
        return 'blue'

def shoot_laser(color):
    if color == 'blue':
        board[8][8].shoot(screen, board)
    else:
        board[0][0].shoot(screen, board)


display = True
move = False
color = 'blue'

while True:
    screen = pygame.display.set_mode((board_size,board_size))
    translate_board(board)

    if display:
        pygame.display.flip()
        display = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        board[0][0].shoot(screen, board)
        display = True

    if pygame.mouse.get_pressed()[0]:
        col, row = pygame.mouse.get_pos()
        row = int(row/square_size)
        col = int(col/square_size)

        if(row == col == 0):
            # Laser functions
            continue

        if(board[row][col] != ' '):
            piece = board[row][col]
            if piece.color == color:
                piece.show_moves(board, screen)
                move = True
                pygame.display.flip()

        if move and valid_coords(piece, (row, col)):
            piece.move((row, col), board)
            display = True
            move = False

            screen = pygame.display.set_mode((board_size,board_size))
            translate_board(board)
            pygame.display.flip()

            shoot_laser(color)
            color = new_color(color)


    #screen.fill((0,0,200)
    #pygame.display.flip()
