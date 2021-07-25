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
                             "distance" : 7}
            }

''' function to generate comparison matrix for each factor
    creat 3 different matrix
    everytime it sorts elements by one of 3 factors
'''
# sorted by time from shortest to greatest
print('Below are the sorted paths from shortest time to greatest: ')
sortedPathByTime = sorted(allPaths, key=lambda x: (allPaths[x]['time']))
print(sortedPathByTime)
print('\n')

# sorted by height from shortest to greatest
print('Below are the sorted paths from shortest height to greatest: ')
sortedPathByHeight = sorted(allPaths, key=lambda x: (allPaths[x]['height']))
print(sortedPathByHeight)
print('\n')


# sorted by distance from shortest to greatest
print('Below are the sorted paths from shortest distance to greatest: ')
sortedPathByDistance = sorted(allPaths, key=lambda x: (allPaths[x]['distance']))
print(sortedPathByDistance)
print('\n')

'''
    The next step is to assign Satty value to each path for each factor
    so for each path, it will be assigned different, if not completely, Satty value three times.
    The rule goes like this: We want to let trashcans lasting for greatest days to be picked up
    as soon as possible (prioritized), piling up greatest height inside the bin to be prioritized
    and routes that require minimum distance should be prioritized.

    In short, longer the trash remains, higher the trash is, and shorter the distance, 
    more prioritized should the route be.

'''
