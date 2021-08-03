#!/usr/local/bin/python3
'''
Step 2 - Auto-generate comparison matrix where it takes urgency degree and
distance as criteria

The rule to calculate Saaty value is by subtracting the smaller value
from larger one and then dividing it up by their sum and multiply the result
by 10. Finally we round the result to get the integer in Saaty Scale.
'''
allPaths = {    'path_1' : { "urgency" : 20,
                             "distance" : 12},
                'path_2' : { "urgency" : 1,
                             "distance" : 14},
                'path_3' : { "urgency" : 30,
                             "distance" : 100},
                'path_4' : { "urgency" : 5,
                             "distance" : 31},
                'path_5' : { "urgency" : 40,
                             "distance" : 52}
            }

urgency_comparisons = {}
distance_comparisons = {}


# function used to generate comparison matrix

def make_cmp(list, cmp_obj):
    for path in list:
        for anopath in list:
            if path[0] >= anopath[0]:
                continue

            global urgency_comparisons
            global distance_comparisons

            if path[1] > anopath[1]:
                dif = (path[1] - anopath[1]) / (path[1] + anopath[1]) * 10
                dif = round(dif)
                if dif < 1:
                    dif = 1
                if dif > 9:
                    dif = 9

                if(cmp_obj == 'urgency'):
                    urgency_comparisons[path[0], anopath[0]] = dif

                if(cmp_obj == 'distance'):
                    distance_comparisons[path[0], anopath[0]] = dif


            else:
                dif = (anopath[1] - path[1]) / (path[1] + anopath[1]) * 10
                dif = round(dif)
                if dif == 0:
                    dif = 1
                if dif > 9:
                    dif = 9
                dif = 1/dif

                if(cmp_obj == 'urgency'):
                    urgency_comparisons[path[0], anopath[0]] = dif

                if(cmp_obj == 'distance'):
                    distance_comparisons[path[0], anopath[0]] = dif




all_urgency = {}
all_distance = {}

# store all paths' urgency
for key, value in allPaths.items():
    for key2, value2 in value.items():
        if key2 == 'urgency':
            all_urgency[key] = value2
            break
# print('Urgency for each path: ' )
# print(all_urgency)


# store all paths' distance
for key, value in allPaths.items():
    for key2, value2 in value.items():
        if key2 == 'distance':
            all_distance[key] = value2
            break

# print('Distance for each path: ' )
# print(all_distance)
# print('\n')

all_urgency = sorted(all_urgency.items())
all_distance = sorted(all_distance.items())
print('The ordered path series with each corresponding to their urgency degree: ')
print(all_urgency)
print('The ordered path series with each corresponding to their distance: ')
print(all_distance)
print('\n')

# make comparisons for two criteria
make_cmp(all_urgency, 'urgency')
make_cmp(all_distance, 'distance')

# print out comparison matrix
print('comparison matrix for urgency: ')
print(urgency_comparisons)
print('comparison matrix for distance: ')
print(distance_comparisons)
print('\n')

# print comparison matrix with criteria vs. goal
criteria_comparisons = {('distance', 'urgency'): 7}
print('comparison matrix for criteria: ')
print(criteria_comparisons)
