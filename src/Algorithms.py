import heapq

def depthfirstsearch(graph, startNode, endNode):
    stack = []
    visited = set([])
    path = []
    while len(stack) != 0:
        top = stack.pop()
        for edges in graph[top]:
            if edges not in visited:
                visited.add(edges)
                stack.append(edges)
                path.append(edges)
    return path


def dijkstras(graph, startNode, endNode):
    distance = dict()
    distance[startNode] = 0
    explored = set()
    parents = dict()
    parents[startNode] = "START"
    path = []
    priorityqueue = heapq.heapify([])
    for vertices in graph.keys():
        if vertices != startNode:
            distance[vertices] = float("inf")
        heapq.heappush(priorityqueue, (vertices, distance[vertices]))

    while len(priorityqueue) != 0:
        top = heapq.heappop(priorityqueue)[0]
        for neighbors in range(0, len(graph)):
            if neighbors != top:
                check = graph[neighbors] + distance[neighbors]
                if check > distance[neighbors]:
                    distance[neighbors] = check
                    parents[neighbors] = top
                if neighbors not in explored:
                    heapq.heappush(priorityqueue, (neighbors, distance[neighbors]))
    currNode = endNode
    path.append(currNode)
    while currNode != startNode:
        currNode = parents[currNode]
        path.append(currNode)
    return path
