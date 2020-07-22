import heapq
import json
import requests


graph = [[0, 1],[1, 0]]
vertexNumber = {"a": 0, "b" : 1}  # in the format "id" -> number
vertexNames = {0 : "a", 1 : "b"}  # in the format number -> "id"
addedVertices = {"a", "b"}
# need first dictionary to keep the graph an adjacency matrix


def newGraph():
    global graph, vertexNames, vertexNumber, addedVertices
    graph = [[0,1],[1,0]]
    vertexNumber = {"a": 0, "b": 1}
    vertexNames = {0: "a", 1: "b"}
    addedVertices = {"a", "b"}
    print(graph)
    return "graphCleared"


def updateGraph(data):
    parsed = json.loads(data)
    data = parsed["data"]
    status = "Pass"
    print(str(graph) + " pre")
    if parsed["Type"] == "V":
        label = data["id"]
        if label not in addedVertices:
            addedVertices.add(label)
            vertexNumber[label] = len(vertexNumber)
            vertexNames[len(vertexNames)] = label
            graph.append([])
            for n in range(0, len(graph)):
                graph[len(graph)-1].append(0)
            for arrays in range(0, len(graph)-1):
                graph[arrays].append(0)
        else:
            status = "Duplicate Vertex"

    elif parsed["Type"] == "E":
        label = data["id"]
        if data["source"] and data["target"] in addedVertices:
            source = vertexNumber[data["source"]]
            target = vertexNumber[data["target"]]
            if graph[source][target] == 0:
                graph[source][target] = int(label)
                graph[target][source] = int(label)
            else:
                status = "Duplicate Edge"
        else:
            if data["source"] not in addedVertices:
                status = "Source Invalid"
            elif data["target"] not in addedVertices:
                status = "Target Invalid"
            else:
                status = "Source and Target Invalid"
    print(str(graph) + " post")
    return status


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
