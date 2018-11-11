import enum
from .Edge import Edge
from .Gamefield import GameField

class Type(enum.Enum):
    unvisited = 'unvisited'
    visited = 'visited'
    blocked = 'blocked'
    start = 'start'
    goal = 'goal'
    portal = 'portal'

class Vertex:

    neighbours = []

    def __init__(self, y_pos,x_pos, type, parentEdge : Edge):

        self.x = x_pos
        self.y = y_pos

        self.parentEdge = parentEdge
        if type not in (Type.unvisited, Type.visited, Type.blocked, Type.start, Type.goal, Type.portal):
             raise ValueError('type not valid')
        self.type = type


    def getNeighbours(gamefield):
        if (gamefield.check_possible_field(y + 1,x) :
            new_neighbour = Vertex(y_pos, x_pos,gamefield.get_vertex_type(new_neighbour),Edge(1,self, new_neighbour))
            outgoing_edges.append(outgoing_edges)
        if (gamefield.check_possible_field(y,x + 1) :
            new_neighbour = Vertex(y_pos, x_pos,gamefield.get_vertex_type(new_neighbour),Edge(1,self, new_neighbour))
            outgoing_edges.append(new_neighbour)
        if (gamefield.check_possible_field(y - 1,x) :
            new_neighbour = Vertex(y_pos, x_pos,gamefield.get_vertex_type(new_neighbour),Edge(1,self, new_neighbour))
            outgoing_edges.append(new_neighbour)
        if (gamefield.check_possible_field(y,x - 1) :
            new_neighbour = Vertex(y_pos, x_pos,gamefield.get_vertex_type(new_neighbour),Edge(1,self, new_neighbour))
            outgoing_edges.append(new_neighbour)


    def __eq__(self, other):
        """Overrides the default implementation"""
        return self.x == other.x and self.y == other.y
