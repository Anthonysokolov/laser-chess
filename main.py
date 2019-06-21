'''
Main file for laser chess
'''
import pygame
import json
from pieces import Deflector, Laser

# Load board setups
with open('setups.json') as f:
    setupsj = json.load(f)

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

for i in setupsj['ace']['red_deflectors'].values():
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
    rloc = rdef_locs[i]
    bloc = bdef_locs[i]

    board[rloc[0]][rloc[1]] = Deflector(rloc,rdef_angles[i],'red',square_size)
    board[bloc[0]][bloc[1]] = Deflector(bloc,bdef_angles[i],'blue',square_size)

board[0][0] = Laser(1,'red', square_size)

def translate_board(board):
    for row in board:
        for pos in row:
            if pos != ' ':
                pos.display(screen)


def print_board(board):
    print("\nBoard")
    for i in board:
        print(i)


def look_for_move(board):
    while True:
        if 1 in pygame.mouse.get_pressed():
            print("pressed")
            col, row = pygame.mouse.get_pos()
            row = int(row/square_size)
            col = int(col/square_size)

            if(board[row][col] == ' '):
                print("RET")
                return row, col




var = 1
while True:
    screen = pygame.display.set_mode((board_size,board_size))
    translate_board(board)
    #board[0][0].shoot(screen, board)

    if var == 1:
        pygame.display.flip()
        var = 0

    pygame.time.delay(1000)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        board[0][0].shoot(screen, board)

    if 1 in pygame.mouse.get_pressed():
        col, row = pygame.mouse.get_pos()
        row = int(row/square_size)
        col = int(col/square_size)
        if(board[row][col] != ' '):
            #board[row][col].move((row+1, col), board)
            board[row][col].show_moves(board, screen)
            pygame.display.flip()
            r, c = look_for_move(board)
            board[row][col].move((r,c),board)


    #screen.fill((0,0,200)
    #pygame.display.flip()


    #x = int(input("Move: "))

'''
# Red deflectors
rdef_locs = [(1,0),(3,2)]
rdef_angles = [0,1]

# Blue deflectors
bdef_locs = [(1,2), (3,0)]
bdef_angles = [2,0]
'''
