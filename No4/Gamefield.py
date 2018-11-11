class GameField:

    self.gamefield_width = len(gamefieldArray[0])
    self.gamefield_height = len(gamefieldArray)

    def __init__(self, fieldString):

    def check_possible_field(y_pos, x_pos):
        return (((y_pos <= gamefield_height and y_pos >= 0) and
                 (x_pos <= gamefield_width and x_pos >= 0 )) and
                (gamefield_array[y_pos][x_pos] != "x"))