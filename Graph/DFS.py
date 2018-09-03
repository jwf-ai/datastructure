# encoding: utf-8

"""
递归实现
"""
def recursion_dfs(graph,visited,path,v):

    for i in range(len(graph[v])):
        if v == 9:
            print(path)
            return
        if graph[v][i] != 0 and visited[i] != 1:
            tmp = path[:]
            tmp.append(i)
            v_t = visited[:]
            v_t[i] = 1
            recursion_dfs(graph,v_t,tmp,i)


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

visited = [0]*len(graph)
visited[0] = 1
recursion_dfs(graph,visited,[0],0)

