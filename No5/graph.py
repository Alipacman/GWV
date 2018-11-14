from vertex import Vertex
from edge import Edge
from gamefield import Gamefield



class Graph:

    vertices = []

    def __init__(self, gamefield : Gamefield, start_y_pos, start_x_pos):
        self.vertices.append(Vertex(start_x_pos, start_y_pos,gamefield.get_vertex_type(start_y_pos, start_x_pos), None))

