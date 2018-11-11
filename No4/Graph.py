from .Vertex import Vertex
from .Edge import Edge




class Graph:

    vertices = []


    def __init__(self, gamefieldArray, start_x_pos, start_y_pos):
        start_vertex = Vertex(start_x_pos, start_y_pos)
        self.gamefieldArray
        self.vertexes.append(start_vertex)
