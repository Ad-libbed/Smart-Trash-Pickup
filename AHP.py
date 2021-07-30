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
time_comparisons = {}
height_comparisons = {}
distance_comparisons = {}

# function used to generate comparison matrix
def make_cmp(dictionary, cmp_obj):
    for key, value in dictionary.items():
        for key2, value2 in dictionary.items():
            if value > value2:
                dif = (value - value2) / value2 * 10
                dif = round(dif)
                if(cmp_obj == 'time'):
                    time_comparisons[key, key2] = [dif]
                if(cmp_obj == 'height'):
                    height_comparisons[key, key2] = [dif]
                if(cmp_obj == 'distance'):
                    distance_comparisons[key, key2] = [dif]

            else:
                dif = (value2 - value) / value * 10
                dif = round(dif)
                if(cmp_obj == 'time'):
                    time_comparisons[key, key2] = [dif]
                if(cmp_obj == 'height'):
                    height_comparisons[key, key2] = [dif]
                if(cmp_obj == 'distance'):
                    distance_comparisons[key, key2] = [dif]


'''
    do a pairwise comparison for allPaths this dictionary for each criterion
    rule: set the smaller one as the base, namely 1, then calculate how greater
    the proportion is the bigger one compared to the smaller one and multiply it
    by 10 and round it to the neartest integer so it's between 1 and 9. If they are equal
    then both of them are 1 in Satty scale.

'''
all_time = {}
all_height = {}
all_distance = {}

# store all paths' time
for key, value in allPaths.items():
    for key2, value2 in value.items():
        if key2 == 'time':
            all_time[key] = value2
print('Time for each path: ' )
print(all_time)

# store all paths' heights
for key, value in allPaths.items():
    for key2, value2 in value.items():
        if key2 == 'height':
            all_height[key] = value2
print('Height for each path: ' )
print(all_height)

# store all paths' distance
for key, value in allPaths.items():
    for key2, value2 in value.items():
        if key2 == 'distance':
            all_distance[key] = value2
print('Distance for each path: ' )
print(all_distance)
print('\n')

# make comparisons for three criteria
make_cmp(all_time, 'time')
make_cmp(all_height, 'height')
make_cmp(all_distance, 'distance')

print(time_comparisons)
print(height_comparisons)
print(distance_comparisons)
