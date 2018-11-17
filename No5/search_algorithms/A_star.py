from collections import deque
import math

def breadth_first_search(start_node):

    closedSet = []
    openSet = [start_node]
    
    while len(openSet) != 0:

        path = frontier.popleft()
        last_node = path[-1]

        if (last_node.is_goal()):
            print("BFS found path: ")
            # print(path)
            return path
        else:
            neighbours = last_node.get_surrounding_neighbours()

            for n in neighbours:
                if not (n in path):
                    new_path = path.copy() + [n]
                    frontier.append(new_path)
    return []