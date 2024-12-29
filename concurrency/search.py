import time
import random

# Generate a large random array
def generate_large_array(size, search_element):
    random.seed(5)
    arr = [random.randint(0, 1_000_000) for _ in range(size)]
    if search_element not in arr:
        arr[random.randint(0, size - 1)] = search_element  # Ensure the element exists
    return arr

# Sequential search for the element
def sequential_search(arr, target):
    start = time.time()
    for i, value in enumerate(arr):
        if value == target:
            end = time.time()
            print(f"Element {target} found at index {i}")
            print(f"Sequential search took {end - start:.2f} seconds")
            return i
    end = time.time()
    print(f"Element {target} not found")
    print(f"Sequential search took {end - start:.2f} seconds")
    return -1

if __name__ == "__main__":
    search_element = 999999
    array = generate_large_array(10_000_000, search_element)
    sequential_search(array, search_element)



#####

import multiprocess as mp
import time
import random
import math

# Generate a large random array
def generate_large_array(size, search_element):
    random.seed(5)
    arr = [random.randint(0, 1_000_000) for _ in range(size)]
    if search_element not in arr:
        arr[random.randint(0, size - 1)] = search_element  # Ensure the element exists
    return arr

# Search a chunk of the array for the target element
def search_chunk(chunk, target, start_index):
    for i, value in enumerate(chunk):
        if value == target:
            return start_index + i
    return -1

# Function to handle concurrent search using multiprocess
def concurrent_search(arr, target, num_workers=32):
    start = time.time()

    # Split the array into chunks
    chunk_size = math.ceil(len(arr) / num_workers)
    chunks = [(arr[i:i + chunk_size], target, i) for i in range(0, len(arr), chunk_size)]

    # Use multiprocess.Pool for parallel processing
    with mp.Pool(num_workers) as pool:
        # Apply the search function to each chunk
        results = pool.starmap(search_chunk, chunks)

    # Check results
    for result in results:
        if result != -1:
            end = time.time()
            print(f"Element {target} found at index {result}")
            print(f"Concurrent search took {end - start:.2f} seconds")
            return result

    end = time.time()
    print(f"Element {target} not found")
    print(f"Concurrent search took {end - start:.2f} seconds")
    return -1

if __name__ == "__main__":
    search_element = 999999
    array = generate_large_array(10_000_000, search_element)
    concurrent_search(array, search_element)


# Threading



import threading
import time
import random
import math

# Generate a large random array
def generate_large_array(size, search_element):
    random.seed(5)
    arr = [random.randint(0, 1_000_000) for _ in range(size)]
    if search_element not in arr:
        arr[random.randint(0, size - 1)] = search_element  # Ensure the element exists
    return arr

# Search a chunk of the array for the target element
def search_chunk(chunk, target, start_index, result_dict, lock):
    for i, value in enumerate(chunk):
        if value == target:
            with lock:
                result_dict["index"] = start_index + i  # Save result with a lock
            return
    return

# Concurrent search for the element using threads
def concurrent_search_with_threads(arr, target, num_workers=32):
    start = time.time()
    chunk_size = math.ceil(len(arr) / num_workers)
    chunks = [(arr[i:i + chunk_size], target, i) for i in range(0, len(arr), chunk_size)]

    threads = []
    result_dict = {"index": -1}  # Shared result dictionary
    lock = threading.Lock()  # Lock for thread-safe access to result_dict

    # Start threads
    for chunk, target, start_index in chunks:
        t = threading.Thread(target=search_chunk, args=(chunk, target, start_index, result_dict, lock))
        threads.append(t)
        t.start()

    # Wait for threads to complete
    for t in threads:
        t.join()

    # Check result
    if result_dict["index"] != -1:
        end = time.time()
        print(f"Element {target} found at index {result_dict['index']}")
        print(f"Concurrent search with threads took {end - start:.2f} seconds")
        return result_dict["index"]

    end = time.time()
    print(f"Element {target} not found")
    print(f"Concurrent search with threads took {end - start:.2f} seconds")
    return -1

if __name__ == "__main__":
    search_element = 999999
    array = generate_large_array(10_000_000, search_element)
    concurrent_search_with_threads(array, search_element)