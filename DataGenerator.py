class DataGenerator:

    # calculation distance between starting point and every shelf
    @staticmethod
    def calculate_starting_distances(starting_coordinates: list, shelves_coordinates: dict) -> dict:
        starting_distances = {}
        for key, value in shelves_coordinates.items():
            # calculation distances between starting point and particular shelf
            starting_distances[key] = abs(starting_coordinates[0] - value[0]) + abs(starting_coordinates[1] - value[1])
        return starting_distances

    # calculation distances between every pair of shelves
    @staticmethod
    def calculate_shelves_distances(shelves_coordinates: dict) -> dict:
        shelves_distances = {}
        # for every single shelf calculate distances to all other shelves
        for key, value in shelves_coordinates.items():
            temporary_distances = {}
            for next_key, next_value in shelves_coordinates.items():
                if key != next_key:
                    temporary_distances[next_key] = abs(next_value[0] - value[0]) + abs(next_value[1] - value[1])
            shelves_distances[key] = temporary_distances
        return shelves_distances

