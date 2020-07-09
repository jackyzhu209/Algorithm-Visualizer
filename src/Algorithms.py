import heapq
import json


graph = [[0, 1], [1, 0]]
vertexNumber = {"a": 0, "b" : 1}  # in the format "id" -> number
vertexNames = {0 : "a", 1 : "b"}  # in the format number -> "id"
# need first dictionary to keep the graph an adjacency matrix


def updateGraph(data):
    parsed = json.loads(data)
    data = parsed["data"]

    if parsed["Type"] == "V":
        label = data["id"]
        vertexNumber[label] = len(vertexNumber)
        vertexNames[len(vertexNames)] = label
        graph.append([])
        for n in range(0, len(graph)):
            graph[len(graph)-1].append(0)
        for arrays in range(0, len(graph)-1):
            graph[arrays].append(0)

    elif parsed["Type"] == "E":
        label = data["id"]
        source = vertexNumber[data["source"]]
        target = vertexNumber[data["target"]]
        graph[source][target] = label

    print(graph)
    print(vertexNames.items())
    print(data)

    return "200"


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
