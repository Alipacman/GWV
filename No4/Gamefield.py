from.Vertex import *
import numpy as np


class GameField:

    gamefieldArray = []

    def __init__(self, fieldString):
        self.gamefieldArray = self.gamefield_str_into_array(fieldString)
        self.gamefield_width = len(gamefieldArray[0])
        self.gamefield_height = len(gamefieldArray)

    def gamefield_str_into_array(gamefield_str):
        """
        Converts a gamefield stored as a string into a gamefield array
        """

        width = gamefield_str.find("\n")
        height = int((len(gamefield_str) - 9)/width)

        gamefield_array = np.empty(shape=[height, width], dtype ="str")

        for y in range(height):
            for x in range(width):
                gamefield_array[y][x] = gamefield_str[((y * width + 1 * y) + x)]

        return gamefield_array

    def gamefield_array_into_str(array):
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

    def check_possible_field(y_pos, x_pos):
        return (gamefield_array[y_pos][x_pos] != "x"))

    def get_vertex_type(vertex : Vertex) -> Type:
        if ((vertex.y <= gamefield_height and vertex.y >= 0) and
          (vertex.x <= gamefield_width and vertex.x >= 0 )):
            return Type.unvisited

        switcher = {
            " ": Type.unvisited,
            ".": Type.visited,
            "1": Type.portal,
            "2": Type.portal,
            "g": Type.goal,
            "s": Type.goal,
        }
        return switcher

