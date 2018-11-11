import enum
from .Edge import Edge
from .Gamefield import GameField

class Vertex_type(enum.Enum):
    unvisited = 'unvisited'
    visited = 'visited'
    blocked = 'blocked'
    start = 'start'
    goal = 'goal'
    portal = 'portal'

class Vertex:

    neighbours = []

    def __init__(self, y_pos,x_pos, parentVertex : Edge, gamefield):

        self.x = x_pos
        self.y = y_pos

        self.parentEdge = Edge(1,parentVertex, self)
        if type not in (Vertex_type.unvisited, Vertex_type.visited, Vertex_type.blocked, Vertex_type.start, Vertex_type.goal, Vertex_type.portal):
             raise ValueError('type not valid')
        self.type = gamefield.get_vertex_type(self)


    def get_neighbours(self, gamefield):
        if (gamefield.check_possible_field(self.y + 1, self.x)):
            neighbour_up = Vertex(self.y + 1, self.x, self, gamefield)
            self.neighbours.append(neighbour_up)
        if (gamefield.check_possible_field(self.y, self.x + 1)):
            neighbour_right = Vertex(self.y, self.x + 1, self, gamefield)
            self.neighbours.append(neighbour_right)
        if (gamefield.check_possible_field(self.y - 1, self.x)):
            neighbour_down = Vertex(self.y - 1, self.x, self, gamefield)
            self.neighbours.append(neighbour_down)
        if (gamefield.check_possible_field(self.y, self.x - 1)):
            neighbour_left = Vertex(self.y, self.x - 1, self, gamefield)
            self.neighbours.append(neighbour_left)
        return self.neighbours

    def check_neighbour_eq_parent(self, other):
        return self.parentEdge.source_vertex == other

    def is_goal(self):
        return self.type == Vertex_type.goal


    def __eq__(self, other):
        """Overrides the default implementation"""
        return self.x == other.x and self.y == other.y
