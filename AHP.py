'''
unit of each factors:
time: days
height: meters
distance: kilometers
'''



# below is just an example of all possible paths given a source and destination
# note this is only one set of one particular source-to-destination situation
# Namely, if there are 5 possible sources, then there would be 5 sets similar like this
allPaths = {    'path_1' : { "time" : 2,
                             "height" : 0.7,
                             "distance" : 12},
                'path_2' : { "time" : 1,
                             "height" : 0.02,
                             "distance" : 14},
                'path_3' : { "time" : 0.2,
                             "height" : 0.3,
                             "distance" : 30},
                'path_4' : { "time" : 3,
                             "height" : 0.5,
                             "distance" : 26},
                'path_5' : { "time" : 8,
                             "height" : 0.29,
                             "distance" : 1}
            }

''' function to generate comparison matrix for each factor
    creat 3 different matrix
    everytime it sorts elements by one of 3 factors
'''
# sorted by time from shortest to greatest
# print('Below are the sorted paths from shortest time to greatest: ')
# sortedPathByTime = sorted(allPaths, key=lambda x: (allPaths[x]['time']))
# print(sortedPathByTime)
# print('\n')
#
# # sorted by height from shortest to greatest
# print('Below are the sorted paths from shortest height to greatest: ')
# sortedPathByHeight = sorted(allPaths, key=lambda x: (allPaths[x]['height']))
# print(sortedPathByHeight)
# print('\n')
#
#
# # sorted by distance from shortest to greatest
# print('Below are the sorted paths from shortest distance to greatest: ')
# sortedPathByDistance = sorted(allPaths, key=lambda x: (allPaths[x]['distance']))
# print(sortedPathByDistance)
# print('\n')

'''
    calculate relative strength for each candidate against each criterion
    for each criterion, add up all paths' values to get the sum which then divides relative strength for one particular path

'''

# for time, height, distance
# get the value of time for each path --> get the sum of them --> divide each path's time by the
sum_time = 0
sum_height = 0
sum_distance = 0
for key, value in allPaths.items():
    sum_time += value['time']
    sum_height += value['height']
    sum_distance += value['distance']

#check correctness of summation. Succeed
print('sum of time, height, distance, respectively: ')
print(sum_time, sum_height, sum_distance)
print('\n')

'''
    calculate relative strength (the result is rounded for the sake of integer rule of Satty scale)
    if the result is 0.0, then all the other result is added by 1
    if the result is greater than 9, then this result is set to 9
'''
rs_time = {}

for key, value in allPaths.items():
    rs = value['time'] / sum_time * 10
    rs_time[key] = round(rs)

out_of_bounds = False
for key, value in rs_time.items():
    if out_of_bounds == True:
        break
    if value == 0.0:
        for key, value in rs_time.items():
            rs_time[key] += 1
            out_of_bounds = True
    if value > 9.0:
        rs_time[key] = 9.0

print('path relative strength against time: ')
print(rs_time)
print('\n')


'''
    calculat relative strength against height
'''
rs_height = {}

for key, value in allPaths.items():
    rs = value['height'] / sum_height * 10
    rs_height[key] = round(rs)

out_of_bounds = False
for key, value in rs_height.items():
    if out_of_bounds == True:
        break
    if value == 0.0:
        for key, value in rs_height.items():
            rs_height[key] += 1
            out_of_bounds = True
    if value > 9.0:
        rs_height[key] = 9.0

print('path relative strength against height: ')
print(rs_height)
print('\n')

'''
    calculat relative strength against distance
    notice that the relative strength against distance is reversed, meaning
    the shortest path has highest relative strength, as opposed to the case
    in previous two.
'''
rs_distance = {}

for key, value in allPaths.items():
    rs = value['distance'] / sum_distance * 10
    rs_distance[key] = round(rs)



print('path relative strength against distance: ')
print(rs_distance)
print('\n')
