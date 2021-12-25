from models.game import game as gm
from minimax import minimax
import pygame
from tkinter import messagebox
from tkinter import *

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
RED = True  #  minimizing player
GREEN = False  # maximizing player
WIDTH = 600
HEIGHT = 600


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game = gm(screen, WIDTH//3, HEIGHT//3)
    board = game.board
    for position in game.positions:
        position.show(white, 0)
        position.show(black, 1)
    pygame.init()
    global end
    end = False
    while not end:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                pygame.quit()
            if pygame.mouse.get_pressed()[0]:
                try:
                    pos = pygame.mouse.get_pos()
                    mousePress(pos, WIDTH, HEIGHT, game, board)
                except AttributeError:
                    pass


def mousePress(x, width, height, game, board):
    global end
    t = x[1]
    w = x[0]
    g1 = t // (width // 3)
    g2 = w // (height // 3)
    move = board[g1][g2]
    try:
        move.show(green, 0)
        ended = game.make_move(move, GREEN)
        print(f"Black moves to {move.row+1},{move.col+1}")
        if ended:
            Tk().wm_withdraw()
            result = messagebox.askokcancel('Game ended', ('would you like to play again?'))
            if result == True:
                main()
            else:
                end = ended
        move = None
        min_out = None
        for position in game.positions:
            out = minimax(position, RED, game.moves)
            if min_out == None:
                min_out = out
                move = position
            elif min_out > out:
                min_out = out
                move = position
        print(f"White moves to {move.row+1},{move.col+1}")
        ended = game.make_move(move, RED)
        move.show(red, 0)
        if ended:
            Tk().wm_withdraw()
            result = messagebox.askokcancel('Game ended', ('would you like to play again?'))
            if result == True:
                main()
            else:
                end = ended
        
    except:
        pass
        