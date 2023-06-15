#import randrange as rand
import random
import pygame
import sys

from numpy.random.mtrand import rand

# The configuration
config = {
    'cell_size': 20,
    'cols': 8,
    'rows': 16,
    'delay': 750,
    'maxfps': 30
}

# Colors
colors = [
    # black
    (0, 0, 0),
    # red
    (255, 0, 0),
    # green
    (0, 150, 0),
    # blue
    (0, 0, 255),
    # orange
    (255, 120, 0),
    # yellow
    (255, 255, 0),
    # purple
    (180, 0, 255),
    # teal
    (0, 220, 220)
]
# Define shapes: wedge, Z, backward Z, L, backward L, bar and square
tetris_shapes = [
    # wedge
    [[1, 1, 1],
     [0, 1, 0]],
    # backward Z
    [[0, 2, 2],
     [2, 2, 0]],
    # Z
    [[3, 3, 0],
     [0, 3, 3]],
    # L
    [[4, 0, 0],
     [4, 4, 4]],
    # backward L
    [[0, 0, 5],
     [5, 5, 5]],
    # Bar
    [[6, 6, 6, 6]],
    # square
    [[7, 7],
     [7, 7]]
]


# Clockwise rotation
def rotate(shape):
    return [[shape[y][x]
             for y in range(len(shape))]
            for x in range(len(shape[0]) - 1, -1, -1)]


# Collision check
def collision(board, shape, offset):
    off_x, off_y = offset
    for cy, row in enumerate(shape):
        for cx, cell in enumerate(row):
            try:
                if cell and board[cy + off_y][cx + off_x]:
                    return True
            except IndexError:
                return True
    return False


# Remove row
def remove_row(board, row):
    del board[row]
    return [[0 for i in range(config['col'])]] + board


# Joining matrixes
def join_matrixes(mat1, mat2, mat2_off):
    off_x, off_y = mat2_off
    for cy, row in enumerate(mat2):
        for cx, val in enumerate(row):
            mat1[cy + off_y - 1][cx + off_x] += val
    return mat1


# New board

def new_board():
    board = [[0 for x in range(config['cols'])]
             for y in range(config['rows'])]
    board += [[1 for x in range(config['cols'])]]
    return board


# Tetris window main
class TetrisApp(object):
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(250, 50)
        self.width = config['cell_size'] * config['cols']
        self.height = config['cell_size'] * config['rows']

        self.screen = pygame.display.set_mode((self.width, self.height))
        from pygame.locals import MOUSEMOTION
        pygame.event.set_blocked(pygame > MOUSEMOTION)  # there were two different imports
        self.init_game()

    def new_stone(self):
        self.stone = tetris_shapes[rand(len(tetris_shapes))]
        self.stone_x = int(config['cols'] / 2 - len(self.stone[0]) / 2)
        self.stone_y = 0

        if collision(self.board,
                     self.stone,
                     (self.stone_x, self.stone_y)):
            self.gameover = True

    # init game(needs better comment
    def init_game(self):
        self.board = new_board()
        self.new_stone()

    # center message
    def center_msg(self, msg):
        for i, line in enumerate(msg.splitlines()):
            msg_image = pygame.font.Font(
                pygame.font.get_default_font(), 12).render(
                line, False, (255, 255, 255), (0, 0, 0))

            msg_center_x, msg_center_y = msg_image.get_size()
            msg_center_x //= 2
            msg_center_y //= 2

            self.screen.blit(msg_image, (
                self.width // 2 - msg_center_x,
                self.height // 2 - msg_center_y + i * 22))

    # draw matrix
    def draw_matrix(self, matrix, offset):
        off_x, off_y = offset
        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                if val:
                    pygame.draw.rect(
                        self.screen, colors[val],
                        pygame.Rect(
                            (off_x + x) *
                            config['cell_size'],
                            (off_y + y) *
                            config['cell_size'],
                            config['cell_size'],
                            config['cell_size']), 0)

    # move
    def move(self, delta_x):
        if not self.gameover and not self.paused:
            new_x = self.stone_x + delta_x
            if new_x < 0:
                new_x = 0
            if new_x > config['cols'] - len(self.stone[0]):
                new_x > config['cols'] - len(self.stone[0])
                if not collision(self.board,
                                 self.stone,
                                 (new_x, self.stone_y)):
                    self.stone_x = new_x

    # quit
    def quit(self):
        self.center_msg("Quit...")
        pygame.display.update()
        sys.exit()

    # drop piece
    def drop(self):
        if not self.gameover and not self.paused:
            self.stone_y += 1
            if collision(self.board,
                         self.stone,
                         (self.stone_x, self.stone_y)):
                self.board = join_matrixes(
                    self.board,
                    self.stone,
                    (self.stone_x, self.stone_y))
                self.new_stone()
                while True:
                    for i, row in enumerate(self.board[:-1]):
                        if 0 not in row:
                            self.board = remove_row(
                                self.board, i)
                            break
                    else:
                            break

    #rotate the piece
    def rotate_stone(self):
        if not self.gameover and not self.paused:
            new_stone = rotate(self.stone)
            if not collision(self.board,
                             new_stone,
                             (self.stone_x, self.stone_y)):
                self.stone = new_stone

    #pause
    def toggle_pause(self):
        self.paused = not self.paused

    #start game
    def start_game(self):
        if self.gameover:
            self.init_game()
            self.gameover = False

    # Movement keys
    def run(self):
        key_actions = {
            'ESCAPE': self.quit,
            'LEFT': lambda: self.move(-1),
            'RIGHT': lambda: self.move(+1),
            'DOWN': self.drop,
            'UP': self.rotate_stone,
            'p': self.toggle_pause,
            'SPACE': self.start_game
        }

        self.gameover = False
        self.paused = False
#replaced "dont_burn_my_cpu" with game_time
        pygame.time.set_timer(pygame.USEREVENT + 1, config['delay'])
        game_time = pygame.time.Clock()
        while 1:
            self.screen.fill((0, 0, 0))
            if self.gameover:
                self.center_msg("""Game Over!
    Press space to continue""")
            else:
                if self.paused:
                    self.center_msg("Paused")
                else:
                    self.draw_matrix(self.board, (0, 0))
                    self.draw_matrix(self.stone,
                                     (self.stone_x,
                                      self.stone_y))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.USEREVENT + 1:
                    self.drop()
                elif event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYDOWN:
                    for key in key_actions:
                        if event.key == eval("pygame.K_"
                                             + key):
                            key_actions[key]()

            game_time.tick(config['maxfps'])

#main run
if __name__== '__main__':
    App = TetrisApp()
    App.run()
