#!/usr/local/bin/python3
from collections import defaultdict
import ast
import itertools
import ahpy

'''
There are in general 3 major steps: A) Produce all valid paths with their three
factors being stored; B) Generate comparison matrix; and C) Use AHP to find best path
where each major step can be divided into several sub-steps.

A-Step 1: create a graph with every edge being recorded; output all possible routes;
store them into allPaths, a dictionary
find all valid paths that contain information about traffic and distance
'''
# Used by DFS function
path_count = 0
count = 0
allPaths = {}
sum_path = 0


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

    def calEdgeNumber(self, u, v):
        return len(self.Edge[u,v])

    def getEdge(self):
        list = self.Edge
        return list

    def getTrafficBT2nodes(self, u, v):
        return self.Traffic[u,v]

    def getEdgesBT2nodes(self, u, v):
        return self.Edge[u,v]

    # remove the first element of the edge set after it's used
    def setEdge(self, u, v):
        self.Edge[u, v].pop(0)

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
            # print(path)
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


'''
A-Step 2: Create class Bin to store each site's height and time

'''
class Bin:

    def __init__(self, number):

        # number of bin sites
        self.number = number

        # default dictionary to store bins
        self.Bins = defaultdict(list)

    # calculate the Urgency degree of a particular trashcan
    def calUrgency(self, site_num):

        # Urgency = 0.4 * time + 0.6 * height
        t = self.getTime(site_num)
        h = self.getTime(site_num)
        value = 0.4 * t + 0.6 * h
        self.Bins[site_num].append(value)

    def updateBin(self, site_num, time, height):
        # site_num = site_num
        # time = time
        # height = height
        # input current status of the bin
        self.Bins[site_num].append(time)
        self.Bins[site_num].append(height)


    def getTime(self, site_num):
        return self.Bins[site_num][0]

    def getHeight(self, site_num):
        return self.Bins[site_num][1]

    def getUrgency(self, site_num):
        return self.Bins[site_num][2]


b = Bin(6)
b.updateBin(0, 1, 80)
b.updateBin(1, 2, 21)
b.updateBin(2, 3, 32)
b.updateBin(3, 4, 34)
b.updateBin(4, 1, 75)
b.updateBin(5, 2, 39)
for i in range(0, b.number):
    b.calUrgency(i)

print("There are %d bins in this graph: "%b.number)
for i in range(0, b.number):
    print("This is Bin %d, and its information is as follows: "%i)
    print("Time the trash remains inside: %d" %b.getTime(i))
    print("Height the trash piles up: %d" %b.getHeight(i))
    print("Urgency degree of this bin: %d" %b.getUrgency(i))
    print("\n")

print('\n')
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# create a graph given in the above diagram
# NOTE: traffic has three string values: "1"--red, "2"--Yello
# "3"--green, denoting degree of traffic stagnancy

g = Graph(6)
g.addEdge(0, 1, 8, 1)
g.addEdge(0, 1, 13, 2)

g.addEdge(0, 2, 8, 3)
g.addEdge(0, 2, 4, 1)

g.addEdge(0, 3, 120, 3)

g.addEdge(0, 4, 12, 1)


g.addEdge(1, 0, 15, 2)

g.addEdge(1, 2, 68, 3)
g.addEdge(1, 2, 21, 3)

g.addEdge(1, 4, 20, 1)
g.addEdge(2, 1, 53, 1)
g.addEdge(2, 3, 12, 2)
g.addEdge(2, 3, 14, 2)
g.addEdge(2, 3, 3, 2)

g.addEdge(2, 4, 32, 1)
g.addEdge(2, 4, 2, 2)

g.addEdge(3, 0, 135, 3)
g.addEdge(3, 2, 12, 3)

g.addEdge(3, 4, 12, 1)
g.addEdge(4, 0, 10, 1)
g.addEdge(4, 1, 7, 2)
g.addEdge(4, 2, 4, 3)
g.addEdge(4, 3, 18, 2)
g.addEdge(4, 5, 89, 1)
g.addEdge(4, 5, 20, 1)
g.addEdge(4, 5, 115, 3)

g.addEdge(5, 4, 15, 1)
g.addEdge(3, 5, 15, 1)
g.addEdge(3, 5, 12, 3)
g.addEdge(5, 3, 6, 1)
g.addEdge(5, 3, 89, 1)



# prints all paths from any given source to any given destination
for i in range(0,g.V):
    for j in range(0,g.V):
        if i != j:
            # print("Followings are different paths from %d to %d :" %(i, j))
            g.printAllPaths(i, j)
            sum_path = sum_path + path_count
            print('There are possible path from %d to %d in total of: %d  ' %(i, j, path_count))
            path_count = 0

print('\n')
print("In total there are %d possible paths"%sum_path)
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# prints all edges between every two vertices
for i in range(0,5):
    for j in range(0,5):
        if i != j:
            print("Followings are different edges between %d to %d :" %(i, j), str(g.printAllEdges(i, j)))

    print('\n')
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")



'''
A-Step 3: Process all possible paths--leave only VALID path--and ultimately store them into [paths]
        Use VALID paths in [paths] to generate permutation of them and assign them corresponding factors:
        Satisfaction, distance, and traffic

'''
# convert string representation of path list back to list type
for key, value in allPaths.items():
    allPaths[key] = ast.literal_eval(allPaths[key])

paths = {}
for key, value in allPaths.items():
    if len(value) == 5:
        paths[key] = value

#remove paths with same order to only one so that every path now remaining
#is unique and valid
d2 = {tuple(v): k for k, v in paths.items()}  # exchange keys, values
paths = {v: list(k) for k, v in d2.items()}
print("Prototype paths below (stored by paths), used for permutation: ")
print(paths)

print('\n')


# permutation of valid paths concerning traffic and distance -- Using trees
# path_permutation stores permutation number for each valid path
path_permutation = {}
def generateAllPaths(proto_paths):

    # for each valid path, find permutation of it
    # calculate number of permutation
    global g
    for key, value in proto_paths.items():
        one_path = value
        num = 1
        for i in range(0, len(one_path) - 1):
            global g
            num = num * g.calEdgeNumber(one_path[i], one_path[i+1])

        global path_permutation
        path_permutation[key] = num



generateAllPaths(paths)
path_permutation = sorted(path_permutation.items())
print('Below are number of permutations for each prototype (stored by path_permutation): ')
print(path_permutation)
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


def produceAllPath(paths):

    # Step 2 & 3 function
    def makeList(list, length):
        list = list
        list_edge_path = []
        list_traffic_path = []
        for i in range(0, length-1):
            global g
            list_edge_path.append(g.getEdgesBT2nodes(list[i], list[i+1]))
            list_traffic_path.append(g.getTrafficBT2nodes(list[i], list[i+1]))
        return list_edge_path, list_traffic_path

    # Step 4 function
    def calSum(permutation_distance, permutation_traffic):
        permutation_distance = permutation_distance
        permutation_traffic = permutation_traffic
        permutation_sum_Distance = []
        permutation_sum_Traffic = []
        for list in permutation_distance:
            permutation_sum_Distance.append(sum(list))

        for list in permutation_traffic:
            permutation_sum_Traffic.append(sum(list))

        return permutation_sum_Distance, permutation_sum_Traffic

    # Step 5 function -- return final path dictionary
    def produce(permutation_sum_Distance, permutation_sum_Traffic, length):
        permutation_sum_Distance = permutation_sum_Distance
        permutation_sum_Traffic = permutation_sum_Traffic
        length = length
        count = 1

        while count <= length:
            name = 'path' + str(count)
            global AllPath
            AllPath[name] = {'Satisfaction' : 1,
                             'Distance' : permutation_sum_Distance[count-1],
                             'Traffic' :  permutation_sum_Traffic[count-1]}
            count = count + 1

    # iterate through paths
    for key, value in paths.items():
        length = len(value)
        list_edge_path, list_traffic_path = makeList(value, length)

        # Step 3
        permutation_distance = list(itertools.product(*list_edge_path))
        permutation_traffic = list(itertools.product(*list_traffic_path))

        # Step 4 -- Calculate sum
        permutation_sum_Distance, permutation_sum_Traffic = calSum(permutation_distance, permutation_traffic)

        # Step 5 -- prodocue dictionary
        produce(permutation_sum_Distance, permutation_sum_Traffic, len(permutation_sum_Distance))

AllPath = {}
produceAllPath(paths)
print("Below are ULTIMATE VALID PATHS, in a total number of %d (stored in AllPath): "%len(AllPath))
print(AllPath)
print("\n")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


'''
B: Generate comparison matrix

'''
traffic_comparisons = {}
distance_comparisons = {}
satisfaction_comparisons = {}

# function used to generate comparison matrix

def make_cmp(list, cmp_obj):
    for path in list:
        for anopath in list:
            if path[0] >= anopath[0]:
                continue

            global traffic_comparisons
            global distance_comparisons
            global satisfaction_comparisons

            if path[1] > anopath[1]:
                dif = (path[1] - anopath[1]) / (path[1] + anopath[1]) * 10
                dif = round(dif)
                if dif < 1:
                    dif = 1
                if dif > 9:
                    dif = 9

                if(cmp_obj == 'traffic'):
                    traffic_comparisons[path[0], anopath[0]] = dif

                if(cmp_obj == 'distance'):
                    distance_comparisons[path[0], anopath[0]] = dif

                if(cmp_obj == 'satisfaction'):
                    satisfaction_comparisons[path[0], anopath[0]] = dif


            else:
                dif = (anopath[1] - path[1]) / (path[1] + anopath[1]) * 10
                dif = round(dif)
                if dif == 0:
                    dif = 1
                if dif > 9:
                    dif = 9
                dif = 1/dif

                if(cmp_obj == 'traffic'):
                    traffic_comparisons[path[0], anopath[0]] = dif

                if(cmp_obj == 'distance'):
                    distance_comparisons[path[0], anopath[0]] = dif

                if(cmp_obj == 'satisfaction'):
                    satisfaction_comparisons[path[0], anopath[0]] = dif




all_traffic = {}
all_distance = {}
all_satisfaction = {}

# store all paths' satisfaction
for key, value in AllPath.items():
    for key2, value2 in value.items():
        if key2 == 'Satisfaction':
            all_satisfaction[key] = value2
            break

# store all paths' distance
for key, value in AllPath.items():
    for key2, value2 in value.items():
        if key2 == 'Distance':
            all_distance[key] = value2
            break


# store all paths' traffic
for key, value in AllPath.items():
    for key2, value2 in value.items():
        if key2 == 'Traffic':
            all_traffic[key] = value2
            break

# print('Distance for each path: ' )
# print(all_distance)
# print('\n')

all_satisfaction = sorted(all_satisfaction.items())
all_distance = sorted(all_distance.items())
all_traffic = sorted(all_traffic.items())
print('The ordered path series with each corresponding to their satisfaction: ')
print(all_satisfaction)
print('The ordered path series with each corresponding to their distance: ')
print(all_distance)
print('\n')
print('The ordered path series with each corresponding to their traffic: ')
print(all_traffic)
print('\n')


# make comparisons for two criteria
make_cmp(all_satisfaction, 'satisfaction')
make_cmp(all_distance, 'distance')
make_cmp(all_traffic, 'traffic')

# print out comparison matrix
print('comparison matrix for satisfaction: ')
print(satisfaction_comparisons)
print('comparison matrix for distance: ')
print(distance_comparisons)
print('comparison matrix for traffic: ')
print(traffic_comparisons)
print('\n')

# print comparison matrix with criteria vs. goal
criteria_comparisons = {('distance', 'satisfaction'): 7, ('distance', 'traffic'): 4, ('traffic', 'satisfaction'): 4  }
print('comparison matrix for criteria: ')
print(criteria_comparisons)
print("\n")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


'''
C: Find best path using AHP

'''

satisfaction = ahpy.Compare('satisfaction', satisfaction_comparisons, precision=3, random_index='dd')
distance = ahpy.Compare('distance', distance_comparisons, precision=3, random_index='dd')
traffic = ahpy.Compare('traffic', traffic_comparisons, precision=3, random_index='dd')
criteria = ahpy.Compare('Criteria', criteria_comparisons, precision=3, random_index='dd')
criteria.add_children([satisfaction, traffic, distance])

print(criteria.target_weights)

report = criteria.report(show=True)

print(report)
