from.Vertex import *

class GameField:

    self.gamefield_width = len(gamefieldArray[0])
    self.gamefield_height = len(gamefieldArray)

    def __init__(self, fieldString):

    def check_possible_field(y_pos, x_pos):
        return (gamefield_array[y_pos][x_pos] != "x"))

    def get_vertex_type(vertex : Vertex) -> Type:
            if ((vertex.y <= gamefield_height and vertex.y >= 0) and
              (vertex.x <= gamefield_width and vertex.x >= 0 )):
                return Type.unvisited
