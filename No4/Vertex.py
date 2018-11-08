import enum

class Type(enum.Enum):
    unvisited = 'unvisited'
    visited = 'visited'
    blocked = 'blocked'
    start = 'start'
    goal = 'goal'
    portal = 'portal'

class Vertex:

    def __init__(self, x_pos, y_pos, type):
        self.x = x_pos
        self.y = y_pos
        if type not in (Type.unvisited, Type.visited, Type.blocked, Type.start, Type.goal, Type.portal):
             raise ValueError('type not valid')
        self.type = type

