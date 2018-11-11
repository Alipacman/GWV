from .Graph import Graph
from .Vertex import Vertex
from .Edge import Edge
from .Gamefield import Gamefield

def main():
    print("Setting up the gamefield...")
    
    #gameFields

    gamefield = Gamefield(open('blatt3_environment.txt', 'r').read())

if __name__ == "__main__":
    main()