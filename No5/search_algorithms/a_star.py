from collections import deque

def a_star_search(start_node):

    frontier = [[start_node]]

    while len(frontier) != 0:

        frontier.sort(key=lambda x: x[-1].a_star_cost, reverse=False)

        path = frontier.pop(0)
        last_node = path[-1]

        if (last_node.is_goal()):
            print("A_star found path: ")
            # print(path)
            return path
        else:
            neighbours = last_node.get_surrounding_neighbours()

            for n in neighbours:
                if not (n in path):
                    new_path = path.copy() + [n]
                    frontier.append(new_path)
    return []
