from vertex import Vertex
from vertex_type import Vertex_type
import numpy as np

class Gamefield:

    gamefield_array = []

    def __init__(self, fieldString):
        self.gamefield_array = self.gamefield_str_into_array(fieldString)
        self.gamefield_width = len(self.gamefield_array[0])
        self.gamefield_height = len(self.gamefield_array)

    def gamefield_str_into_array(self, gamefield_str):
        """
        Converts a gamefield stored as a string into a gamefield array
        """

        width = gamefield_str.find("\n")
        height = int(len(gamefield_str)/width) 

        gamefield_array = np.empty(shape=[height, width], dtype ="str")

        for y in range(height):
            for x in range(width):
                gamefield_array[y][x] = gamefield_str[((y * width + 1 * y) + x)]

        return gamefield_array

    def gamefield_array_into_str(self, array):
        """
        Converts a gamefield arry into a string representation
        """

        gamfield_str = ""

        for y in range(len(array)):
            if y != 0:
                gamfield_str = gamfield_str + "\n"
            for x in range(len(array[0])):
                gamfield_str = gamfield_str + str(array[y][x])

        return gamfield_str

    def check_possible_field(self, y_pos, x_pos):
        return not (y_pos >= self.gamefield_height or y_pos < 0 or
                x_pos >= self.gamefield_width or x_pos < 0 or self.gamefield_array[y_pos][x_pos] == "x")

    def get_vertex_type(self, vertex : Vertex) -> Vertex_type:

        if (vertex.y >= self.gamefield_height or vertex.y < 0 or
            vertex.x >= self.gamefield_width or vertex.x < 0):
            return Vertex_type.unvisited

        switcher = {
            " ": Vertex_type.unvisited,
            ".": Vertex_type.visited,
            "1": Vertex_type.portal,
            "2": Vertex_type.portal,
            "g": Vertex_type.goal,
            "s": Vertex_type.unvisited,
        }
        return switcher.get(self.gamefield_array[vertex.y][vertex.x])


    def find_start_index(self):
        for y in range(self.gamefield_height):
            for x in range(self.gamefield_width):
                if self.gamefield_array[y][x] == "s":
                    return (y,x)


    def print_path(self, path : [Vertex]):
        for vertex in path:
            self.gamefield_array[vertex.y][vertex.x] = "."
        print (self.gamefield_array_into_str(self.gamefield_array))