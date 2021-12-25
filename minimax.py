from models.game import game as gm

def minimax(position, minimizing_player, moves):
    game = gm()
    game.set_state(moves)
    position = game.board[position.row][position.col]
    end = game.make_move(position, minimizing_player)
    if end:
        return position.outcome

    if  minimizing_player:
        max_out = -2
        for child in game.positions:
            outcome = minimax(child, not minimizing_player, game.moves)
            max_out = max(max_out, outcome)
        return max_out
    else:
        min_out = 2
        for child in game.positions:
            outcome = minimax(child, not minimizing_player, game.moves)
            min_out = min(min_out, outcome)
        return min_out