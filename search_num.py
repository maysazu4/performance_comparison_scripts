import time
import random
from draw_results import *

# Linear search algorithm
def linear_search(list, target):
    """Performs a linear search to find the index of the target number in the list.

    Args:
        list (list): The list to search in.
        target: The target number to search for.

    Returns:
        int: The index of the target number in the list, or -1 if not found.
    """
    for i, num in enumerate(list):
        if num == target:
            return i
    return -1

# Binary search algorithm
def binary_search(list, num):
    """Performs a binary search to find the index of the target number in the sorted list.

    Args:
        list (list): The sorted list to search in.
        num: The target number to search for.

    Returns:
        int: The index of the target number in the list, or -1 if not found.
    """
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == num:
            return mid
        elif list[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Function to calculate execution time of search operations
def calculate_results(list, target, func):
    """Calculates the time taken to perform the search operation using the specified function.

    Args:
        list (list): The list to search in.
        target: The target number to search for.
        func (function): The search algorithm function to be used.

    Returns:
        float: The total execution time in seconds.
    """
    start_time = time.perf_counter()
    func(list, target)
    end_time = time.perf_counter()
    total_time = round(end_time - start_time, 2)
    return total_time

# Function to generate data (sorted list of random numbers)
def generate_data(size):
    """Generates a sorted list of random numbers with the specified size.

    Args:
        size (int): The size of the list to generate.

    Returns:
        list: A sorted list of random numbers.
    """
    return sorted(random.sample(range(0, size), size))

if __name__ == "__main__":
    # Lists to store results for linear and binary search algorithms
    results1 = []
    results2 = []

    # Iterate through 10 different orders of magnitude (from 1 to 10)
    for magnitude in range(1, 9):
        size = 10 ** magnitude
        data = generate_data(size)  # Generate a sorted list of random numbers for each size
        target = random.randint(1, size - 1)  # Choose a random target within the range of the list
        # Calculate execution time for linear search algorithm
        time1 = calculate_results(data, target, linear_search)
        results1.append((size, time1))
        # Calculate execution time for