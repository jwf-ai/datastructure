# encoding: utf-8

from queue import Queue

graph = [
    #0  1  2  3  4  5  6  7  8  9
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 0]
]

def printGraph(graph):
    for i in range(len(graph)):
        s = str(i)+":"
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                s = s + str(j) + ","
        print(s)

def BFS(graph, target):
    visit = [0] * len(graph)
    q = Queue()
    q.put(0)
    visit[0] = 1
    parent = [-1] * len(graph)
    dist = [0] * len(graph)
    while q.empty() == False:
        point = q.get()

        for i in range(len(graph[point])):
            if graph[point][i] == 1 and visit[i] == 0:
                q.put(i)
                visit[i] = 1
                parent[i] = point
                dist[i] = dist[point] + 1

    return dist,parent

def showPath(parent, start, end):
    res = []
    if parent[end] == -1:
        print("No path")
    else:
        tmp = end

        while tmp != start:
            res.append(tmp)
            tmp = parent[tmp]
        res.append(start)
        res.reverse()
    return res


if __name__ == "__main__":
    #printGraph(graph)
    target = 8
    dist,parent = BFS(graph,target)
    print("distance:",dist[target])
    print(showPath(parent,0,target))