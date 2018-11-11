import enum

class Type(enum.Enum):
    unvisited = 'unvisited'
    visited = 'visited'
    blocked = 'blocked'
    start = 'start'
    goal = 'goal'
    portal = 'portal'

class Vertex:

    def __init__(self, y_pos,x_pos, type, parentEdge):

        self.x = x_pos
        self.y = y_pos
        self.parentEdge = parentEdge
        if type not in (Type.unvisited, Type.visited, Type.blocked, Type.start, Type.goal, Type.portal):
             raise ValueError('type not valid')
        self.type = type

    def getNeighbours(gamefield):
    neighbours = []
    if (currentVertex.y + 1,currentVertex.x):
        neighbours.append(Vertex(y_pos, x_pos) (y_pos + 1, x_pos)
        if check_possible_field(currentVertex.y + 1,currentVertex.x):

            neighbours.append()
    return neighbours

    def __eq__(self, other):
        """Overrides the default implementation"""
    if isinstance(other, Number):
        return self.number == other.number
    return False
