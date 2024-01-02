import pygame
from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN



WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS


RED_PIECE_IMAGE = pygame.image.load("red_piece.jpg")
WHITE_PIECE_IMAGE = pygame.image.load("white_piece.jpg")
CROWN_IMAGE = pygame.image.load("crown.png")

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("dama")

GREY = (128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        img = RED_PIECE_IMAGE if self.color == RED else WHITE_PIECE_IMAGE
        img = pygame.transform.scale(img, (SQUARE_SIZE - self.PADDING*2, SQUARE_SIZE - self.PADDING*2))
        rect = img.get_rect()
        rect.center = (self.x, self.y)
        win.blit(img, rect)
        if self.king:
            crown = pygame.transform.scale(CROWN_IMAGE, (SQUARE_SIZE - self.PADDING*5, SQUARE_SIZE - self.PADDING*5))
            crown_rect = crown.get_rect()
            crown_rect.center = (self.x, self.y)
            win.blit(crown, crown_rect)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)
