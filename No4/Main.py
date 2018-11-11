from .Graph import Graph
from .Vertex import Vertex
from .Edge import Edge
import numpy as np

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

def main():
    print("Setting up the gamefield...")
    
    #gameFields
    gamefield = gamefield_str_into_array(open('blatt3_environment.txt', 'r').read())

if __name__ == "__main__":
    main()