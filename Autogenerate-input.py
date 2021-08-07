'''
Program to automate the process of generating traffic and distance value
for each bin pair
'''

from collections import defaultdict
from itertools import chain
import random
import scipy.stats as stats

# This class represents a directed graph
# using adjacency list representation
allPaths = {}
count = 1

class Graph:

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

        self.Edge = defaultdict(list)

        self.Traffic = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v, distance, traffic):
        self.graph[u].append(v)
        self.Edge[u,v].append(distance)
        self.Traffic[u,v].append(traffic)

    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''
    def printAllPathsUtil(self, u, d, visited, path):

        # Mark the current node as visited and store in path
        visited[u]= True
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            global allPaths
            global count
            name = 'path' + str(count)
            allPaths[name] = str(path)
            count = count + 1
            # print path
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i]== False:
                    self.printAllPathsUtil(i, d, visited, path)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u]= False


    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):

        # Mark all the vertices as not visited
        visited =[False]*(self.V)

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)

'''
Create two functions that can generate traffic and distances
'''
# function to generate a random, or multiple values for distance
def assignDistanceAndTraffic(node_i, node_j):
    # stores all distances between two nodes
    list_Distance = []

    # stores all traffics between two nodes, in compliance with the distance list
    list_Traffic = []

    # for each node pair, there will be no more than 3 edges
    num = random.randrange(1,3,1)

    # function to generate a random number either 7 or 3 for traffic
    def assignTraffic(times):
        list = []
        for i in range(times):
            if random.randrange(1,11,1) <= 5:
                list.append(3)
            else:
                list.append(7)
        return list

    list_Traffic = assignTraffic(num)

    for i in range(0, num):
        a, b = 1, 15
        mu, sigma = 5, 3
        dist = stats.truncnorm((a - mu) / sigma, (b - mu) / sigma, loc=mu, scale=sigma)

        value = dist.rvs(1)
        result = round(value[0])

        global g
        g.addEdge(node_i, node_j, result, list_Traffic[i])
        # list_Distance.append(result)




# Create a graph given in the above diagram
g = Graph(10)
for i in range(10):
    for j in range(10):
        if (i != j) and j != 9:
            assignDistanceAndTraffic(i,j)

sum = 0
for i in range(10):
    for j in range(10):
        if i != j:
            length_i_j = len(allPaths)
            g.printAllPaths(i, j)
            length_i_j = len(allPaths) - length_i_j
            print("There are in total of %d paths from %d to %d"%(length_i_j, i, j))



# This code is contributed by Neelam Yadav
print(count)







# # finding duplicate values
# # from dictionary using set
# rev_dict = {}
# for key, value in allPaths.items():
#     rev_dict.setdefault(value, set()).add(key)
#
#
# result = set(chain.from_iterable(
#          values for key, values in rev_dict.items()
#          if len(values) > 1))
#
# # printing result
# print("resultant key", str(result))
