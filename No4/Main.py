from .Graph import Graph
from .Vertex import Vertex
from .Edge import Edge



#TODO: convert this to: txt_into_Graph

#Methods for string array switch
def gamefield_into_array(height, width):

    gamefield_array = np.empty(shape=[height, width], dtype ="str")

    for y in range(height):
        for x in range(width):
            gamefield_array[y][x] = gamefield[((y * width + 1 * y) + x)]

    return gamefield_array

def array_into_gamefield(array):

    gamfield_str = ""

    for y in range(len(array)):
        if y != 0:
            gamfield_str = gamfield_str + "\n"
        for x in range(len(array[0])):
            gamfield_str = gamfield_str + str(array[y][x])

    return gamfield_str


#gameFields
gamefield = open('blatt3_environment.txt', 'r').read()

def main():
    print("starting main")

if __name__ == "__main__":
    main()