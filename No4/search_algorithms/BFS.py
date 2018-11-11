from collections import deque

def breadth_first_search(graph, start_node):
    frontier = deque([[start_node]])

    while (len(frontier) != 0)
        path = frontier.popleft()
        last_node = path[-1]

        if (last_node.is_goal):
            return path
        else:
            neighbours = last_node.get_neighbours

            for n in neighbours:
                pass
            

