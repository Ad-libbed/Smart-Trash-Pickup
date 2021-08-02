'''
Step 1: create a graph with every edge being recorded; output all possible routes;
store them into allPaths, a dictionary
find all valid paths that contain information about traffic and distance
'''
# Used by DFS function
path_count = 0
count = 0
allPaths = {}

from collections import defaultdict

# This class represents a directed graph
# using adjacency list representaion
class Graph:

    def __init__(self, vertices):
        # number of vertices
        self.V = vertices

        # default dictionary to store graph
        self.Graph = defaultdict(list)

        # default edge length between two vertices
        self.Edge = defaultdict(list)

        # defualt traffic between two vertices
        self.Traffic = defaultdict(list)

    def getEdge(self):
        list = self.Edge
        return list

        # function to add an edge to graph
    def addEdge(self, u, v, distance, traffic):
        self.Graph[u].append(v)

        # in case there are more than one edge between two vertices
        self.Edge[u,v].append(distance)

        self.Traffic[u,v].append(traffic)



    def printAllPathsUntill(self, u, d, visited, path):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)


        #If current vertex is same as destination, then print current path[]
        if u == d:
            global path_count
            global allPaths
            path_count = path_count + 1
            print(path)
            name = 'path' + str(path_count)
            allPaths[name] = str(path)

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


    def printAllEdges(self, s, e):
        list = self.Edge[s,e]
        return list


# create a graph given in the above diagram
# NOTE: traffic has three string values: "1"--red, "2"--Yello
# "3"--green, denoting degree of traffic stagnancy
g = Graph(5)
g.addEdge(0, 1, 12, 1)
g.addEdge(0, 1, 13, 2)

g.addEdge(0, 2, 14, 3)
g.addEdge(0, 2, 4, 1)

g.addEdge(0, 3, 20, 3)

g.addEdge(0, 4, 12, 1)


g.addEdge(1, 0, 10, 2)

g.addEdge(1, 2, 12, 3)
g.addEdge(1, 2, 21, 3)

g.addEdge(1, 4, 12, 1)
g.addEdge(2, 1, 12, 1)
g.addEdge(2, 3, 12, 2)

g.addEdge(2, 4, 12, 1)
g.addEdge(2, 4, 20, 2)

g.addEdge(3, 0, 12, 3)
g.addEdge(3, 2, 12, 3)

g.addEdge(3, 4, 12, 1)
g.addEdge(4, 0, 10, 1)
g.addEdge(4, 1, 7, 2)
g.addEdge(4, 2, 4, 3)
g.addEdge(4, 3, 18, 2)
s = 0
d = 3

# prints all paths from any given source to any given destination
for i in range(0,5):
    for j in range(0,5):
        if i != j:
            print("Followings are different paths from %d to %d :" %(i, j))
            g.printAllPaths(i, j)
            print('There are paths in total of: ' + str(path_count))
            path_count = 0
print('\nAfter deleting all the invalid paths, here are the final possible routes: ')

for key, value in allPaths.items():
    allPaths[key] = list(value.split(" "))
for key, value in allPaths.items():
    if len(value) != 5:
        del allPaths[key]

#remove paths with same order to only one so that every path now remaining
#is unique and valid
d2 = {tuple(v): k for k, v in allPaths.items()}  # exchange keys, values
allPaths = {v: list(k) for k, v in d2.items()}
print(allPaths)
print('\n')

newPaths = []
#permutation of valid paths concerning traffic and distance -- Using trees







# prints all edges between every two vertices
for i in range(0,5):
    for j in range(0,5):
        if i != j:
            print("Followings are different edges between %d to %d :" %(i, j))
            print(g.printAllEdges(i, j))

    print('\n')


# filter all allPaths

















'''
Step 2: process every path first by checking 1) if they miss any important bin
2) calculate their Urgency value for late use in AHP

# NOTE: all paths are stored in allPaths, this dictionary
# NOTE: Step 2 is independent of step 1

'''

# input each transhcan site's time and height

class Bins:

    def __init__(self, number):

        # number of bin sites
        self.N = number

        # default dictionary to store bins
        self.Bins = defaultdict(list)


    def updateBin(self, site_num, time, height):

        # input current status of the bin
        self.Bins[site_num] = {'height' : height,
                               'time' : time}

    # calculate the Urgency degree of a particular trashcan
    def calUrgency(self, site_num):

        # Urgency = 0.4 * time + 0.6 * height
        t = self.getTime(site_num)
        h = self.getTime(site_num)
        value = 0.4 * t + 0.6 * h
        self.Bins[site_num] = {'urgency' : value }

    def getTime(self, site_num):
        return self.Bins[site_num]['time']

    def getHeight(self, site_num):
        return self.Bins[site_num]['height']

# update Bins
b = Bins(5)
b.updateBin(1, 10, 3)
b.updateBin(2, 2, 2)
b.updateBin(3, 15, 9)
b.updateBin(4, 1, 7)
b.updateBin(5, 20, 10)

# calculate each transhcan's Urgency
for i in range(1, b.N + 1):
    b.calUrgency(i)
for i in range(1, b.N + 1):
    print("trash site %d has an urgency of %.4f" %(i, b.Bins[i]['urgency']))




'''
Step 3: Use AHP to find the optimal route
sub-step: 1) auto-generate comparison matrix
          2) use matrix generated to start AHP

'''

urgency_comparisons = {}
fuel_comparisons = {}
