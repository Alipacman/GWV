def depth_first_search(start_node):

    frontier = [[start_node]]

    while len(frontier) != 0:
        path = frontier.pop()
        last_node = path[-1]

        if (last_node.is_goal):
            return path
        else:
            neighbours = last_node.get_neighboursqwewe

            for n in neighbours:
                frontier.insert(0, path.copy().append(n))
    return []



