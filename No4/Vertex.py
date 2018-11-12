from edge import Edge
from vertex_type import Vertex_type

class Vertex:

    def __init__(self, y_pos, x_pos, parentVertex, gamefield):

        self.x = x_pos
        self.y = y_pos

        self.parentEdge = Edge(1,parentVertex, self)
        self.vertex_type = gamefield.get_vertex_type(self)
        self.gamefield = gamefield

        self.neighbours = []

        if self.vertex_type not in (Vertex_type.unvisited, Vertex_type.visited, Vertex_type.blocked, Vertex_type.start, Vertex_type.goal, Vertex_type.portal):
             raise ValueError('type not valid')


    def get_neighbours(self):

        if (self.gamefield.check_possible_field(self.y + 1, self.x)):
            neighbour_down = Vertex(self.y + 1, self.x, self, self.gamefield)
            if neighbour_down.vertex_type == Vertex_type.portal:
                self.get_portal_neighbour(neighbour_down)
            else:
                self.neighbours.append(neighbour_down)
        if (self.gamefield.check_possible_field(self.y, self.x + 1)):
            neighbour_right = Vertex(self.y, self.x + 1, self, self.gamefield)
            if neighbour_right.vertex_type == Vertex_type.portal:
                self.get_portal_neighbour(neighbour_right)
            else:
                self.neighbours.append(neighbour_right)
        if (self.gamefield.check_possible_field(self.y - 1, self.x)):
            neighbour_up = Vertex(self.y - 1, self.x, self, self.gamefield)
            if neighbour_up.vertex_type == Vertex_type.portal:
                self.get_portal_neighbour(neighbour_up)
            else:
                self.neighbours.append(neighbour_up)
        if (self.gamefield.check_possible_field(self.y, self.x - 1)):
            neighbour_left = Vertex(self.y, self.x - 1, self, self.gamefield)
            if neighbour_left.vertex_type == Vertex_type.portal:
                self.get_portal_neighbour(neighbour_left)
            else:
                self.neighbours.append(neighbour_left)
        return self.neighbours

    def is_goal(self):
        return self.vertex_type == Vertex_type.goal


    def get_portal_neighbour(self, portal_neighbour):
        portal_exit_loc = self.gamefield.find_portal_exit(portal_neighbour)
        portal_exit = Vertex(portal_exit_loc[0], portal_exit_loc[1], self, self.gamefield)
        self.neighbours.append(portal_exit)

    def __eq__(self, other):
        """Overrides the default implementation"""
        if type(other) is Vertex:
            return self.x == other.x and self.y == other.y
        return False
