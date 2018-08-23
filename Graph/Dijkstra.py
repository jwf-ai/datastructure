# encoding: utf-8

class Dijkstar(object):
    def __init__(self, adj_mat, begin_v):
        self.adj_mat = adj_mat
        self.begin_v = begin_v
        self.n = len(adj_mat)
        self.dist = adj_mat[begin_v]
        self.visit = [False] * self.n
        self.path = self._init_path()
        self.max = float("inf")

    def _init_path(self):
        path = []
        for i in range(self.n):
            if i != self.begin_v and self.dist[i] < float("inf"):
                path.append(self.begin_v)
            else:
                path.append(-1)
        return path

    def find_shortest_path(self):
        self.visit[self.begin_v] = True
        for i in range(self.n-1):

            # 找到距离当前节点最近的节点
            shortest_v = self.begin_v
            minDist = self.max
            for j in range(self.n):
                if self.visit[j] == False and self.dist[j] < minDist:
                    shortest_v = j
                    minDist = self.dist[j]

            self.visit[shortest_v] = True

            for k in range(self.n):
                # 找到最近节点相连的节点
                w = self.adj_mat[shortest_v][k]
                if self.visit[k] == False and w < self.max \
                    and self.dist[shortest_v] + w < self.dist[k]:
                    self.dist[k] = self.dist[shortest_v] + w
                    self.path[k] = shortest_v

        return self._print_shortest_path()

    def _print_shortest_path(self):

        res = []
        for i in range(self.n):
            if i != self.begin_v:
                end_v = i
                shortest_dist = self.dist[i]

                if shortest_dist == self.max:
                    res.append((self.begin_v, end_v, shortest_dist, "No path"))
                    continue

                path = []
                j = i
                while True:
                    path.append(j+1)
                    if j == self.begin_v:
                        break
                    else:
                        j = self.path[j]
                path.reverse()
                path = "->".join(list(str(k) for k in path))
                res.append((self.begin_v,end_v,shortest_dist,path))

        return res



if __name__ == "__main__":
    inf = float("inf")
    adjacencyMat = [
        [0, inf, 10, inf, 30, 100],
        [inf, 0, 5, inf, inf, inf],
        [inf, inf, 0, 50, inf, inf],
        [inf, inf, inf, 0, inf, 10],
        [inf, inf, inf, 20, 0, 60],
        [inf, inf, inf, inf, inf, 0]
    ]

    dijkstra = Dijkstar(adjacencyMat,0)

    res = dijkstra.find_shortest_path()
    for s,e,d,p in res:
        print("%d -> %d: %0.1f, %s"%(s+1,e+1,d,p))