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

        self.a_star_cost = self.a_star_cost()


    def get_surrounding_neighbours(self):
        if (self.gamefield.check_possible_field(self.y + 1, self.x)):
            self.get_neighbour(self.y + 1, self.x)
        if (self.gamefield.check_possible_field(self.y, self.x + 1)):
            self.get_neighbour(self.y, self.x + 1)
        if (self.gamefield.check_possible_field(self.y - 1, self.x)):
            self.get_neighbour(self.y - 1, self.x)
        if (self.gamefield.check_possible_field(self.y, self.x - 1)):
            self.get_neighbour(self.y, self.x - 1)
        return self.neighbours

    def get_neighbour(self, y_pos, x_pos):
        neighbour = Vertex(y_pos, x_pos, self, self.gamefield)
        if neighbour.vertex_type == Vertex_type.portal:
            self.get_portal_neighbour(neighbour)
        else:
            self.neighbours.append(neighbour)

    def is_goal(self):
        return self.vertex_type == Vertex_type.goal


    def get_portal_neighbour(self, portal_neighbour):
        #print(self.gamefield.find_portal_exit(portal_neighbour))
        portal_exit_loc = self.gamefield.find_portal_exit(portal_neighbour)
        portal_exit = Vertex(portal_exit_loc[0], portal_exit_loc[1], self, self.gamefield)
        self.neighbours.append(portal_exit)

    def getCost(self, akk = 0):
        if not (self.parentEdge.source_vertex == None):
            akk += self.parentEdge.weight
            return self.parentEdge.source_vertex.getCost(akk)
        return akk

    def a_star_cost (self):
        return self.getCost() + self.gamefield.manhattan_distance(self)


    def __eq__(self, other):
        """Overrides the default implementation"""
        if type(other) is Vertex:
            return self.x == other.x and self.y == other.y
        return False
