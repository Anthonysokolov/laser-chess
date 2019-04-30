'''
Class definitions for laser chess pieces
'''
class Deflector:
    def __init__(self, pos, angle, symbol):
        self.row = pos[0]
        self.col = pos[1]
        # For the angle
        # 1 is when the mirror is in the top right corner, 2 is top left,
        # 3 is bottom left, 4 is bottom right
        self.angle = angle
        self.symbol = symbol

    def plot_piece(self, board):
        board[self.row][self.col] = self.symbol

    def remove_piece(self, board):
        board[self.row][self.col] = ' '

    def rotate(self, new_angle):
        self.angle = new_angle

    def move(self, pos, board):
        if self.move_valid(pos):
            self.remove_piece(board)
            self.row = pos[0]
            self.col = pos[1]
            self.plot_piece(board)
        else:
            return False

    def move_valid(self, pos):
        if abs(self.row - pos[0]) <= 1 and abs(self.col - pos[1]) <= 1:
            return True
        else:
            return False

    def calc_angle(self, dir):
        if dir == 'u':
            if self.angle == 3:
                return 'r'
            if self.angle == 4:
                return 'l'
        elif dir == 'd':
            if self.angle == 1:
                return 'l'
            if self.angle == 2:
                return 'r'
        elif dir == 'r':
            if self.angle == 1:
                return 'u'
            if self.angle == 4:
                return 'd'
        elif dir == 'l':
            if self.angle == 2:
                return 'u'
            if self.angle == 3:
                return 'd'
        else:
            return 'rm'



class Laser:
    def __init__(self, color):
        self.row = 8
        self.col = 8
        self.color = color

    def plot_piece(self, board):
        board[self.row][self.col] = 'L'

    def shoot_laser(self, board, pieces):
        r = self.row
        c = self.col
        dir = 'u'
        count = 0
        while True:
            r, c = self.move_laser(r,c,dir)
            if self.laser_valid(r,c) == False:
                break
            if board[r][c] in [' ','*']:
                board[r][c] = '*'
            else:
                piece = pieces[board[r][c]]
                angle = piece.angle
                dir = self.calc_angle(dir, angle)
                if dir == 'rm':
                    piece.remove_piece(board)
                    break


    def laser_valid(self,r,c):
        board_size = 9
        if r < 0 or c < 0:
            return False
        if r >= board_size or c >= board_size:
            return False
        return True


    def move_laser(self, r, c, dir):
        '''
        Moves the laser beam one space in a given direction
        '''
        if dir == "u":
            return (r -1, c)
        if dir == "d":
            return (r + 1, c)
        if dir == "l":
            return (r, c - 1)
        if dir == "r":
            return (r, c + 1)

    def calc_angle(self, dir, angle):
        if dir == 'u':
            if angle == 3:
                return 'r'
            if angle == 4:
                return 'l'
        elif dir == 'd':
            if angle == 1:
                return 'l'
            if angle == 2:
                return 'r'
        elif dir == 'r':
            if angle == 1:
                return 'u'
            if angle == 4:
                return 'd'
        elif dir == 'l':
            if angle == 2:
                return 'u'
            if angle == 3:
                return 'd'
        return 'rm'


class Switch:
    def __init__(self, pos, angle, symbol):
        self.pos = pos
        self.angle = angle
        self.symbol = symbol

    def plot_piece(self, board):
        x = self.pos[0]
        y = self.pos[1]

        board[x][y] = self.symbol

    def remove_piece(self, board):
        x = self.pos[0]
        y = self.pos[1]

        board[x][y] = ' '
