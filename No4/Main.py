from .Graph import Graph
from .Vertex import Vertex
from .Edge import Edge

def main():
    print("Setting up the gamefield...")
    
    #gameFields
    gamefield = gamefield_str_into_array(open('blatt3_environment.txt', 'r').read())

if __name__ == "__main__":
    main()