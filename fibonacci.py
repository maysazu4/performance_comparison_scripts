import time
from draw_results import *


# Standard Fibonacci calculation function
def fibonacci(n):
    """Computes the nth Fibonacci number using the standard recursive approach.

    Args:
        n (int): The index of the Fibonacci number to compute.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Optimized Fibonacci calculation function using memoization
def fib(n, memo={}):
    """Computes the nth Fibonacci number using an optimized approach with memoization.

    Args:
        n (int): The index of the Fibonacci number to compute.
        memo (dict): A dictionary to store computed Fibonacci numbers for memoization.

    Returns:
        int: The nth Fibonacci number.
    """
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]


# Function to calculate execution time of standard Fibonacci calculation
def calculate_results(num , func):
    """Calculates the time taken to compute Fibonacci numbers up to 'num' using the specified function.

    Args:
        num (int): The maximum index of Fibonacci number to compute.
        func (function): The Fibonacci calculation function to be used.

    Returns:
        float: The total execution time in seconds.
    """
    start_time = time.perf_counter()
    func(num)
    end_time = time.perf_counter()
    total_time = round(end_time - start_time, 2)
    return total_time


# Function to calculate execution time of optimized Fibonacci calculation with memoization
def calculate_results1(num ,memo ,func):
    """Calculates the time taken to compute Fibonacci numbers up to 'num' using the specified function with memoization.

    Args:
        num (int): The maximum index of Fibonacci number to compute.
        memo (dict): A dictionary to store computed Fibonacci numbers for memoization.
        func (function): The Fibonacci calculation function to be used.

    Returns:
        float: The total execution time in seconds.
    """
    start_time = time.perf_counter()
    memo[num] = func(num, memo)
    end_time = time.perf_counter()
    total_time = round(end_time - start_time, 2)
    return total_time


if __name__ == "__main__":
    # Lists to store results for standard and optimized Fibonacci algorithms
    results1 = []
    results2 = []

    # Iterate through Fibonacci numbers from 1 to 48 with a step of 4
    for i in range(1, 49, 4):
        # Calculate execution time for standard Fibonacci algorithm
        result1 = calculate_results(i, fibonacci)
        # Calculate execution time for optimized Fibonacci algorithm with memoization
        result2 = calculate_results1(i, {}, fib)
        # Append results to respective lists
        results1.append((i, result1))
        results2.append((i, result2))

    # Draw comparison graphs and save results to a CSV file
    draw_results(results1, results2, 'fibonacci', 'improved fibonacci', 'fibonacci.csv')