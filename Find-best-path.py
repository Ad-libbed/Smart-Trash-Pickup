#!/usr/local/bin/python3
import ahpy
 # set up comparison matrix with alternatives vs. criterion
time_comparisons = {('path_1', 'path_2'): 1, ('path_5', 'path_4'): 1, ('path_1', 'path_3'): 8.0, ('path_3', 'path_2'): 7.0, ('path_1', 'path_4'):   1, ('path_1', 'path_5'): 1, ('path_2', 'path_5'): 1, ('path_2', 'path_4'):    1, ('path_3', 'path_4'): 9.0, ('path_3', 'path_5'): 9}

height_comparisons = {('path_1', 'path_2'): 9.0, ('path_5', 'path_4'): 3.0, ('path_1', 'path_3'): 4.0, ('path_3', 'path_2'): 9.0, ('path_1', 'path_4'):   2.0, ('path_1', 'path_5'): 4.0, ('path_2', 'path_5'): 9.0, ('path_2',         'path_4'): 9.0, ('path_3', 'path_4'): 3.0, ('path_3', 'path_5'): 1}

distance_comparisons = {('path_1', 'path_2'): 1, ('path_5', 'path_4'): 1, ('path_1', 'path_3'): 1, ('path_3', 'path_2'): 1, ('path_1', 'path_4'): 1,    ('path_1', 'path_5'): 1, ('path_2', 'path_5'): 1, ('path_2', 'path_4'): 1,    ('path_3', 'path_4'): 1, ('path_3', 'path_5'): 1}

 # set up comparison matrix with criteria vs. goal
criteria_comparisons = {('time', 'height'): 5, ('time', 'distance'): 1/5, ('height', 'distance'): 1/7}

 # calculate priorities
time = ahpy.Compare('time', time_comparisons, precision=3, random_index='saaty')
height = ahpy.Compare('height', height_comparisons, precision=3, random_index='saaty')
distance = ahpy.Compare('distance', distance_comparisons, precision=3, random_index='saaty')
criteria = ahpy.Compare('Criteria', criteria_comparisons, precision=3, random_index='saaty')
criteria.add_children([time, height, distance])

print(criteria.target_weights)

report = criteria.report(show=True)

print(report)
