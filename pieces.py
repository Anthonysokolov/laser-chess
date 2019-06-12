'''
Class definitions for laser chess pieces
'''
import pygame

class Deflector:
    def __init__(self, pos, angle, color, square_size):
        self.row = pos[0]
        self.col = pos[1]

        if color == 'red':
            self.image = pygame.image.load("rtriangle.png").convert_alpha()
        else:
            self.image = pygame.image.load("btriangle.png").convert_alpha()

        # The number of the angle refers to where the mirror is
        # 0 = top left , 1 = top right, 2 = bottom right, 3 = bottom left
        self.angle = angle
        self.rotate(self.angle * 90)

        self.color = color

        self.square_size = square_size

    def rotate(self, deg):
        self.image = pygame.transform.rotate(self.image, deg)

    def display(self, screen):
        screen.blit(self.image,(self.col*self.square_size, self.row*self.square_size))

    def move(self, new_coord, board):
        board[new_coord[0]][new_coord[1]] = board[self.row][self.col]
        board[self.row][self.col] = ' '

        self.row = new_coord[0]
        self.col = new_coord[1]

    def show_moves(self, board, screen):
        for i in range(self.row - 1, self.row + 2):
            for j in range(self.col - 1, self.col + 2):
                try:
                    if board[i][j] == ' ':
                        pos = (j*self.square_size + 50, i*self.square_size + 50)
                        pygame.draw.circle(screen, (255, 0, 0), pos, 25)
                except IndexError:
                    continue


class Laser:
    def __init__(self, angle, color, square_size):
        self.row = 0
        self.col = 0

        if color == 'red':
            self.image = pygame.image.load("rlaser.png").convert_alpha()

        self.angle = angle
        self.square_size = square_size

    def rotate(self):
        self.image = pygame.transform.rotate(self.image, VALUE)

    def display(self, screen):
        screen.blit(self.image,(self.col*self.square_size, self.row*self.square_size))

    def shoot(self, screen, board):
        '''
        Shoots and displays a laser beam on the board
        '''
        red = (255,0,0)
        adjust = self.square_size / 2
        start = [self.col*self.square_size + adjust, self.row*self.square_size + adjust]
        stop = [start[0], start[1] + self.square_size]

        dir = 'south'

        while True:
            pygame.draw.line(screen, red, start, stop)
            pygame.display.flip()
            pygame.time.delay(100)

            # Note: pygame coords are (column, row)
            r = int(stop[1]/self.square_size)
            c = int(stop[0]/self.square_size)

            if (r not in range(9) or c not in range(9)):
                break

            if board[r][c] != ' ':
                dir = self.new_dir(dir, board[r][c].angle)

            if dir != 'end':
                start, stop = self.new_coords(start, stop, dir)
            else:
                board[r][c] = ' '
                break


    def new_dir(self, laser_dir, mirror_angle):
        '''
        Calculates the new direction of a laser beam when it hits a mirror
        '''
        if laser_dir == 'north':
            if mirror_angle == 3:
                return 'east'
            if mirror_angle == 2:
                return 'west'
        if laser_dir == 'south':
            if mirror_angle == 0:
                return 'east'
            if mirror_angle == 1:
                return 'west'
        if laser_dir == 'east':
            if mirror_angle == 1:
                return 'north'
            if mirror_angle == 2:
                return 'south'
        if laser_dir == 'west':
            if mirror_angle == 0:
                return 'north'
            if mirror_angle == 3:
                return 'south'

        return 'end'


    def new_coords(self, start, stop, dir):
        '''
        Calculates the new coordinates for drawing a laser beam
        The beam is drawn one square at a time
        '''
        start = [x for x in stop]

        if dir == 'north':
            stop[1] -= self.square_size
        elif dir == 'south':
            stop[1] += self.square_size
        elif dir == 'east':
            stop[0] += self.square_size
        elif dir == 'west':
            stop[0] -= self.square_size

        return start, stop
