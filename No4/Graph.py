from .Vertex import Vertex
from .Edge import Edge




class Graph:

    edges = []
    vertexes = []

    def __init__(self, start_x_pos, start_y_pos):
        start_vertex = Vertex(start_x_pos, start_y_pos)
        self.vertexes.append(start_vertex)


