import multiprocess
import time
import random

def fetch_data(source):
    """
    Simulate an I/O-bound operation in a process.
    Just like in threads, but since this is a new process,
    it runs in parallel at the OS level without GIL contention.
    """
    print(f"Process {multiprocess.current_process().name} fetching from {source}...")
    time.sleep(random.uniform(0.5, 1.0))  # I/O wait simulation
    return f"data_from_{source}"

def process_data(data):
    """
    Simulate a CPU-bound processing step.
    Processes can truly speed this up in parallel since each process has its own GIL.
    """
    # Just a dummy CPU-bound task: sum of squares
    # The larger this computation, the more you benefit from multiprocessing over threading.
    total = sum(i * i for i in range(200000))
    return f"processed_{data}_{total}"

def producer(sources, queue):
    """
    Producer function: fetch data and put it into a multiprocess.Queue
    for consumers. Very similar to threading but we use multiprocess.Queue.
    """
    for src in sources:
        data = fetch_data(src)
        queue.put(data)
    # Signal no more data
    queue.put(None)

def consumer(queue, results_list, lock):
    """
    Consumer function: read from the queue, process data, store results.
    Uses lock to synchronize writes to the shared list managed by a Manager.
    """
    while True:
        data = queue.get()
        if data is None:
            queue.put(None)  # Put None back to signal other consumers to stop
            break
        processed = process_data(data)
        # With multiprocess, objects from a Manager are accessible by all processes.
        with lock:
            results_list.append(processed)

def main():
    # Using a Manager to share data structures safely between processes.
    manager = multiprocess.Manager()
    results = manager.list()      # Shared list
    lock = manager.Lock()         # Shared lock
    work_queue = manager.Queue()  # Shared queue for producer-consumer pattern

    sources = ["url1", "url2", "url3", "url4", "url5"]

    # Create one producer process
    p = multiprocess.Process(target=producer, args=(sources, work_queue))

    # Create consumer processes
    # Multiprocess scales better for CPU-bound tasks
    consumers = [multiprocess.Process(target=consumer, args=(work_queue, results, lock)) for _ in range(3)]

    start = time.time()

    p.start()
    for c in consumers:
        c.start()

    # Wait for the producer to finish
    p.join()

    # Wait for consumers to finish
    for c in consumers:
        c.join()

    end = time.time()

    print("All processes finished.")
    print("Results:", list(results))
    print(f"Time taken: {end - start:.2f} seconds")

if __name__ == "__main__":
    # IMPORTANT: On Windows and macOS, if you use multiprocessing,
    # you must protect the entry point of the program to avoid infinite recursion.
    # The __name__ == "__main__" guard is crucial.
    main()
