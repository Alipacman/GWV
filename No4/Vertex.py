from edge import Edge
from vertex_type import Vertex_type

class Vertex:

    neighbours = []

    def __init__(self, y_pos,x_pos, parentVertex, gamefield):

        self.x = x_pos
        self.y = y_pos

        self.parentEdge = Edge(1,parentVertex, self)
        self.vertex_type = gamefield.get_vertex_type(self)
        self.gamefield = gamefield

        if self.vertex_type not in (Vertex_type.unvisited, Vertex_type.visited, Vertex_type.blocked, Vertex_type.start, Vertex_type.goal, Vertex_type.portal):
             raise ValueError('type not valid')


    def get_neighbours(self):
        if (self.gamefield.check_possible_field(self.y + 1, self.x)):
            neighbour_up = Vertex(self.y + 1, self.x, self, self.gamefield)
            if (self.check_neighbour_eq_parent(neighbour_up)):
                self.neighbours.append(neighbour_up)
        if (self.gamefield.check_possible_field(self.y, self.x + 1)):
            neighbour_right = Vertex(self.y, self.x + 1, self, self.gamefield)
            if (self.check_neighbour_eq_parent(neighbour_right)):
                self.neighbours.append(neighbour_right)
        if (self.gamefield.check_possible_field(self.y - 1, self.x)):
            neighbour_down = Vertex(self.y - 1, self.x, self, self.gamefield)
            if (self.check_neighbour_eq_parent(neighbour_down)):
                self.neighbours.append(neighbour_down)
        if (self.gamefield.check_possible_field(self.y, self.x - 1)):
            neighbour_left = Vertex(self.y, self.x - 1, self, self.gamefield)
            if (self.check_neighbour_eq_parent(neighbour_left)):
                self.neighbours.append(neighbour_left)
        return self.neighbours

    def check_neighbour_eq_parent(self, other):
        return self.parentEdge.source_vertex == other

    def is_goal(self):
        return self.vertex_type == Vertex_type.goal


    def __eq__(self, other):
        """Overrides the default implementation"""
        if type(other) is Vertex:
            return self.x == other.x and self.y == other.y
        return False
