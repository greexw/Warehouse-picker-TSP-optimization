import random
from DataGenerator import DataGenerator
from RandomSearch import RandomSearch

# starting point of warehouse worker
starting_point = [16, 4]
# position of shelves (x, y)
shelves_coordinates = {'a': [3, 2],
          'b': [2, 6],
          'c': [8, 6],
          'd': [12, 2],
          'e': [13, 6],
          'f': [10, 5],
          'g': [1, 4],
          'h': [4, 8]}

starting_distances = DataGenerator.calculate_starting_distances(starting_point, shelves_coordinates)
shelves_distances = DataGenerator.calculate_shelves_distances(shelves_coordinates)

while True:
    print("---------------------------------------------")
    print("1. Print distances from start point")
    print("2. Print distances from each point to other points")
    print("3. Calculate best trace using random search")
    choice = input("Your choice: ")

    if choice == '1':
        print(starting_distances)
    elif choice == '2':
        print(shelves_distances)
    elif choice == '3':
        number_of_iterations = int(input("Enter number of iterations:"))
        RandomSearch.find_distances(starting_distances, shelves_distances, number_of_iterations)
    elif choice == '8':
        break
    else:
        print("Invalid choice!")

