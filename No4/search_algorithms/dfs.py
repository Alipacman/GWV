def depth_first_search(start_node):

    frontier = [[start_node]]
 
    while len(frontier) != 0:

        path = frontier.pop()
        last_node = path[-1]

        if (last_node.is_goal()):
            print("DFS found path: ")
            print(path)
            return path
        else:
            neighbours = last_node.get_neighbours()

            for n in neighbours:
                if not (n in path):
                    new_path = path.copy() + [n]
                    frontier.append(new_path)
    return []