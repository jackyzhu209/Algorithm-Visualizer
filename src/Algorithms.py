import heapq
import json


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
    return "graphCleared"


def updateGraph(data):
    parsed = json.loads(data)
    data = parsed["data"]
    status = "Pass"
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
        if data["source"] in addedVertices and data["target"] in addedVertices:
            source = vertexNumber[data["source"]]
            target = vertexNumber[data["target"]]
            if graph[source][target] == 0:
                graph[source][target] = int(label)
                graph[target][source] = int(label)
            else:
                status = "Duplicate Edge"
        else:
            if data["source"] not in addedVertices and data["target"] not in addedVertices:
                status = "Source and Target Invalid"
            elif data["source"] not in addedVertices:
                status = "Source Invalid"
            elif data["target"] not in addedVertices:
                status = "Target Invalid"
            else:
                status = "Source and Target Invalid"
    return status


def depthfirstsearch(graph, startNode, endNode):
    stack = [startNode]
    visited = set([startNode])
    path = [startNode]
    while len(stack) != 0:
        top = stack.pop()
        if top not in visited:
            visited.add(top)
            for edges in range(0, len(graph)):
                if graph[top][edges] != 0:
                    stack.append(edges)
                    path.append(edges)
    return path



def breadthfirstsearch(graph, startNode, endNode):
    start = vertexNumber[startNode]
    end = vertexNumber[endNode]
    queue = [start]
    visited = set([start])
    parents = {}
    path = []

    while len(queue) != 0:
        popped = queue.pop(0)
        if popped != end:
            for neighbors in range(0, len(graph)):
                if graph[popped][neighbors] != 0 and neighbors not in visited:
                    visited.add(neighbors)
                    parents[neighbors] = popped
                    queue.append(neighbors)
        else:
            path.append(vertexNames[end])
            currNode = end
            while currNode != start:
                path.append(vertexNames[parents[currNode]])
                currNode = parents[currNode]
            path.reverse()
            print(path)
            return {"result": path}
    return {"result": "not connected"}


def dijkstras(graph, startNode, endNode):
    distance = dict()
    distance[startNode] = 0
    explored = set()
    parents = dict()
    parents[startNode] = "START"
    path = []
    priorityqueue = heapq.heapify([])
    for vertices in range(0,len(graph)):
        if vertices != startNode:
            distance[vertices] = float("inf")
        heapq.heappush(priorityqueue, (vertices, distance[vertices]))

    while len(priorityqueue) != 0:
        top = heapq.heappop(priorityqueue)[0]
        for neighbors in range(0, len(graph)):
            if neighbors != top:
                check = graph[neighbors][top] + distance[neighbors]
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
    path.reverse()
    return {"result": path}


def runAlgorithm(data):
    parsed = json.loads(data)
    algo = parsed["Algo"]
    start = parsed["Start"]
    end = parsed["End"]
    status = ""
    print(graph)
    if start not in addedVertices and end not in addedVertices:
        status = {"result": "Start and End Node Invalid"}
    elif start not in addedVertices:
        status = {"result": "Start Node Invalid"}
    elif end not in addedVertices:
        status = {"result": "End Node Invalid"}
    elif start and end in addedVertices:
        if algo == "BFS":
            status = breadthfirstsearch(graph, start, end)
        elif algo == "DFS":
            status = depthfirstsearch(graph, start, end)
        elif algo == "Dijkstra":
            status = dijkstras(graph, start, end)
    return json.dumps(status)
