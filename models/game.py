from .position import position

class game:
    def __init__(self, screen=0, w=0, h=0):
        self.board = list()
        self.positions = list()
        self.moves = list()
        for i in range(3):
            self.board.append([])
            for j in range(3):
                self.board[i].append(position(i, j, screen, w, h))
                self.positions.append(self.board[i][j])

    def set_state(self, moves):
        for move in moves:
            m = move["position"]
            m = self.board[m.row][m.col]
            self.make_move(m, move["player"])
        

    def row_check(self, position):
        is_end = True
        for i in range(3):
            player = self.board[i][0].occupied_by
            if player != "0":
                for j in range(3):
                    if self.board[i][j].occupied_by != player:
                        is_end = False
            else:
                is_end = False
            if is_end:
                position.update(is_end, player)
                return True
            is_end = True
        return False


    def col_check(self, position):
        is_end = True
        for i in range(3):
            player = self.board[0][i].occupied_by
            if player != "0":
                for j in range(3):
                    if self.board[j][i].occupied_by != player:
                        is_end = False
            else:
                is_end = False
            if is_end:
                position.update(is_end, player)
                return True
            is_end = True
        return False
        

    def diagonal_check(self, position):
        is_end =  True
        player = self.board[0][0].occupied_by
        if player != "0":
            for i in range(3):
                if self.board[i][i].occupied_by != player :
                    is_end = False
        else:
            is_end = False
        
        if is_end:
            position.update(is_end, player)
            return True

        is_end =  True
        player = self.board[0][2].occupied_by
        if player != "0":
            for i in range(3):
                if self.board[i][2-i].occupied_by != player :
                    is_end = False
        else:
            is_end = False
        
        if is_end:
            position.update(is_end, player)
            return True
        return False


    def draw_check(self, position):
        if self.positions == []:
            position.is_end = True
            position.outcome = 0
            return True
        return False

    def make_move(self, position, maximizing_player):
        if maximizing_player:
            self.positions.remove(position)
            position.occupied_by = 'W'
            self.moves.append({"position": position, "player": maximizing_player})
        else:
            self.positions.remove(position)
            position.occupied_by = "B"
            self.moves.append({"position": position, "player": False})  #  Player False automatically means maximizing player
        
        if  not self.row_check(position):
            if not self.col_check(position):
                if not self.diagonal_check(position):
                    if not self.draw_check(position):
                        return False
                    else:
                        return True
                else:
                    return True
            else:
                return True
        else:
            return True