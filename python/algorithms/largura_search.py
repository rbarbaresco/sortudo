# -*- coding: utf-8 -*-
from python.algorithms.map import Map


def largura_search(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)


# print(largura_search(graph, '1', '11'))

map = Map()
map.print_matrix()
from datetime import datetime
print('START', datetime.utcnow())
print(largura_search(map.get_graph(), (0, 0), (5, 5)))
print('END  ', datetime.utcnow())

