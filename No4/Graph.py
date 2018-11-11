from .Vertex import Vertex
from .Edge import Edge
from .Gamefield import GameField



class Graph:

    vertices = []

    def __init__(self, gamefield : GameField, start_y_pos, start_x_pos):
        self.vertices.append(Vertex(start_x_pos, start_y_pos,gamefield.get_vertex_type(y_pos, x_pos), None))
        self.gamefieldArray

