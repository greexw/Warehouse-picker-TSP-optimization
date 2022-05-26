import random

# start point of warehouse worker
start_point = [16, 4]
# position of shelfs (x, y)
points = {'a': [3, 2],
          'b': [2, 6],
          'c': [8, 6],
          'd': [12, 2],
          'e': [13, 6],
          'f': [10, 5],
          'g': [1, 4],
          'h': [4, 8]}


def calculate_points_distances(points: dict) -> dict:
    points_distances = {}
    for key, value in points.items():
        # distances for start point calculation using Manhattan metric
        start_distances[key] = abs(start_point[0] - value[0]) + abs(start_point[1] - value[1])
        temporary_distances = {}
        # distances for other points to current point calculation using Manhattan metric
        for key2, value2 in points.items():
            if key != key2:
                temporary_distances[key2] = abs(value2[0] - value[0]) + abs(value2[1] - value[1])
        points_distances[key] = temporary_distances
    return points_distances


def calculate_start_distances(points: dict, start_point: list) -> dict:
    start_distances = {}
    for key, value in points.items():
        # distances for start point calculation using Manhattan metric
        start_distances[key] = abs(start_point[0] - value[0]) + abs(start_point[1] - value[1])
        temporary_distances = {}
    return start_distances

start_distances = calculate_start_distances(points, start_point)
points_distances = calculate_points_distances(points)

trace = ['a', 'c', 'e', 'g']


# calculate total distances for traces given in first argument
def calculate_distances(random_traces: dict, start_distances: dict, points_distances: dict) -> dict:
    distances = {}
    print(random_traces)
    for element in random_traces:
        current_distance = 0
        for i in range(len(random_traces[element])):
            if i == 1:
                current_distance += start_distances[random_traces[element][i]]
            elif i == 0:
                continue
            else:
                current_point = random_traces[element][i]
                previous_point = random_traces[element][i-1]
                current_distance += points_distances[previous_point][current_point]
        distances[element] = current_distance
    return distances


# find the best trace for points given in first argument
def random_search(trace: list, start_distances: dict, points_distances: dict, number_of_samples: int):
    random_traces = {}
    for i in range(number_of_samples):
        current_trace = []
        current_trace.append('start')
        while len(current_trace) != len(trace)+1:
            next_point = random.choice(trace)
            if next_point not in current_trace:
                current_trace.append(next_point)
        random_traces[i] = current_trace

    distances = calculate_distances(random_traces, start_distances, points_distances)
    best_distance = min(distances, key=distances.get)
    print(f"Best trace: {random_traces[best_distance]}")
    print(f"Length: {distances[best_distance]}")


while True:
    print("---------------------------------------------")
    print("1. Print distances from start point")
    print("2. Print distances from each point to other points")
    print("3. Calculate best trace using random search")
    choice = input("Your choice: ")

    if choice == '1':
        print(start_distances)
    elif choice == '2':
        print(points_distances)
    elif choice == '3':
        number_of_iterations = int(input("Enter number of iterations:"))
        random_search(trace, start_distances, points_distances, number_of_iterations)
    elif choice == '8':
        break
    else:
        print("Invalid choice!")

