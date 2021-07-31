#Print all paths from a given source to a destination in a graph/map

from collections import defaultdict


# This class represents a directed graph
# using adjacency list representaion
class Graph:

    def __init__(self, vertices):
        # number of vertices
        self.V = vertices

        # default dictionary to store graph
        self.Graph = defaultdict(list)

        # function to add an edge to graph
    def addEdge(self, u, v):
        self.Graph[u].append(v)


        '''A recursive function to print all paths from 'u' to 'd'
        visited[] keeps track of vertices in current path.
        path[] stores actual vertices and path_index is current index in path[].
        '''
    def printAllPathsUntill(self, u, d, visited, path):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        #If current vertex is same as destination, then print current path[]
        if u == d:
            print path
        else:
            # If current vertex is not destination,
            # recur for all vertices adjecent to this vertex
            for i in self.Graph[u]:
                if visited[i] == False:
                    self.printAllPathsUntill(i, d, visited, path)

        # remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    # prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):

        # mark all the vertices as not visited
        visited = [False]*(self.V)

        # create an array to store paths
        path = []

        # call the recursive function to print all paths
        self.printAllPathsUntill(s, d, visited, path)

# create a graph given in the above diagram
g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(0, 4)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(1, 4)
g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(3, 0)
g.addEdge(3, 2)
g.addEdge(3, 4)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(4, 2)
g.addEdge(4, 3)
s = 0
d = 3

print("Followings are different paths from %d to %d :" %(s, d))
g.printAllPaths(s, d)
