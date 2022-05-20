# start point of warehouse worker
start_point = [16, 4]
# position of shelfs (x, y)
points = {'a': [3, 2],
          'b': [2, 6],
          'c': [8, 6],
          'd': [12, 2],
          'e': [13, 6]}

start_distances = {}
points_distances = {}
for key, value in points.items():
    # distances for start point calculation using Manhattan metric
    start_distances[key] = abs(start_point[0]-value[0]) + abs(start_point[1]-value[1])
    temporary_distances = {}
    # distances for other points to current point calculation using Manhattan metric
    for key2, value2 in points.items():
        if key != key2:
            temporary_distances[key2] = abs(value2[0]-value[0]) + abs(value2[1]-value[1])
    points_distances[key] = temporary_distances


print(start_distances)
print(points_distances)