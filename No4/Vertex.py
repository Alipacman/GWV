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


    def getNeighbours(self, gamefield):
        if (gamefield.check_possible_field(self.y + 1, self.x)):
            neighbour_up = Vertex(self.y_pos + 1, self.x_pos, self, gamefield)
            self.outgoing_edges.append(self.neighbour_up)
        if (gamefield.check_possible_field(self.y, self.x + 1)):
            neighbour_right = Vertex(self.y_pos, self.x_pos + 1, self, gamefield)
            self.outgoing_edges.append(neighbour_right)
        if (gamefield.check_possible_field(self.y - 1, self.x)):
            neighbour_down = Vertex(self.y_pos - 1, self.x_pos, self, gamefield)
            self.outgoing_edges.append(neighbour_down)
        if (gamefield.check_possible_field(self.y, self.x - 1)):
            neighbour_left = Vertex(self.y_pos, self.x_pos - 1, self, gamefield)
            self.outgoing_edges.append(neighbour_left)

    def check_neighbour_eq_parent(self, other):
        return self.parentEdge.source_vertex == other


    def __eq__(self, other):
        """Overrides the default implementation"""
        return self.x == other.x and self.y == other.y
