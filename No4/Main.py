from vertex import Vertex
from edge import Edge
from gamefield import Gamefield
from search_algorithms.bfs import breadth_first_search
from search_algorithms.dfs import depth_first_search

def main():
    print("Setting up the gamefield...")
    
    # read gamefield from file
    gamefield = Gamefield(open('blatt4_environment_b.txt', 'r').read())

    # Construct graph and find start node
    start_index = gamefield.find_start_index()
    start_node = Vertex(start_index[0], start_index[1], None, gamefield)
    
    #dfs_path = depth_first_search(start_node)
    #gamefield.print_path(dfs_path)

    bfs_path = breadth_first_search(start_node)
    gamefield.print_path(bfs_path)

if __name__ == "__main__":
    main()