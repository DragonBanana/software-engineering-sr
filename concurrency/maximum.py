import copy
import random
import time

# Generate a large random array
def generate_large_array(size):
    return [random.randint(0, 1_000_000) for _ in range(size)]

# Find the maximum value in the array sequentially
def find_max_sequential(arr):
    start = time.time()
    max_value = max(arr)  # Sequentially find the maximum value
    end = time.time()
    print(f"Sequential max value: {max_value}")
    print(f"Time taken (sequential): {end - start:.2f} seconds")
    return max_value

if __name__ == "__main__":
    array_size = 10_000_000  # Size of the array
    array = generate_large_array(array_size)
    find_max_sequential(array)


##

import multiprocess as mp
import random
import time
import math

# Generate a large random array
def generate_large_array(size):
    return [random.randint(0, 1_000_000) for _ in range(size)]

# Find the maximum value in a chunk
def find_max_in_chunk(chunk):
    return max(chunk)

# Concurrent implementation to find the maximum value
def find_max_concurrent(arr, num_workers=4):
    start = time.time()

    # Split the array into chunks
    chunk_size = math.ceil(len(arr) / num_workers)
    chunks = [copy.copy(arr[i:i + chunk_size]) for i in range(0, len(arr), chunk_size)]

    # Use multiprocess.Pool to process chunks concurrently
    with mp.Pool(num_workers) as pool:
        partial_maxima = pool.map(find_max_in_chunk, chunks)  # Each process finds the max of its chunk

    # Find the maximum value among all partial maxima
    overall_max = max(partial_maxima)

    end = time.time()
    print(f"Concurrent max value: {overall_max}")
    print(f"Time taken (concurrent): {end - start:.2f} seconds")
    return overall_max

if __name__ == "__main__":
    array_size = 100_000_000  # Size of the array
    num_processes = 32        # Number of worker processes

    array = generate_large_array(array_size)

    print("Running sequential version:")
    find_max_sequential(array)

    print("\nRunning concurrent version:")
    find_max_concurrent(array, num_processes)
