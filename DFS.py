#finds all possible routes from Start to End
#input: n = 4, e = 6
# 0 -> 1, 0 -> 2, 2 -> 0, 2 -> 3, 3 -> 3
# output: DFS from vertex 1 to vertex 3

from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v)

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFSUtil(neighbor, visited)

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)

g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

print("Following is DFS from (Starting vertex 2)")
g.DFS(2)
