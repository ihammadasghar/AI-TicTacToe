from pygame.draw import rect
from pygame.display import update

class position:
    def __init__(self, row, col, screen, w, h):
        self.row = row
        self.col = col
        self.outcome = None
        self.occupied_by = "0"
        self.is_end = False
        self.screen = screen
        self.width = w
        self.height = h

    def update(self, is_end, winner):
        if is_end:
                self.is_end = True
                if winner == "W":
                    self.outcome = -1  #  White wins
                else:
                    self.outcome = 1  #  Black wins
                return True
    
    def show(self, color, st):
        rect(self.screen, color, (self.col * self.width, self.row * self.height, self.width, self.height), st)
        update()