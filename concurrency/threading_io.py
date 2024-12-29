import threading
import time
import random

def fetch_data(source):
    print(f"Starting fetch from {source}")
    time.sleep(random.uniform(0.5, 1.0))  # Simulate I/O delay
    data = f"data_from_{source}"
    print(f"Finished fetch from {source}")
    return data

def basic_thread_example():
    sources = ["url1", "url2", "url3", "url4"]
    threads = []
    results = []

    # We can store results either by attaching to thread or using a mutable object
    # Let's store results in a global list for simplicity.
    # (We'll improve this later.)
    results_lock = threading.Lock()

    def worker(src):
        data = fetch_data(src)
        with results_lock:
            results.append(data)

    for src in sources:
        t = threading.Thread(target=worker, args=(src,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All threads have finished.")
    print("Results:", results)

import concurrent.futures
import time
import requests

# A function that fetches content from a URL (same as before)
def fetch_url(url):
    print(f"Fetching: {url}")
    response = requests.get(url)
    return len(response.content)

# Concurrent version: Using ThreadPoolExecutor
def concurrent_fetch(urls):
    start = time.time()
    results = []
    # Create a thread pool
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks and collect results as they complete
        futures = {executor.submit(fetch_url, url): url for url in urls}
        for future in concurrent.futures.as_completed(futures):
            url = futures[future]
            try:
                result = future.result()
                results.append(result)
                print(f"Finished fetching {url}: {result} bytes")
            except Exception as e:
                print(f"Error fetching {url}: {e}")
    end = time.time()
    print(f"Concurrent: Fetched {len(urls)} URLs in {end - start:.2f} seconds")
    return results

if __name__ == "__main__":
    urls = [
        "https://example.com",
        "https://example.org",
        "https://www.wikipedia.org",
        "https://www.python.org",
        "https://www.github.com"
    ]
    concurrent_fetch(urls)


###############################################
###############################################
# 2
###############################################
###############################################

def race_condition_example():
    shared_list = []
    sources = ["url1", "url2", "url3", "url4"]
    threads = []

    # Without a lock, concurrent append operations might be okay in CPython,
    # but let's assume we do more complex operations that cause issues.

    def worker(src):
        data = fetch_data(src)
        # Potentially unsafe complex operation:
        temp = shared_list[:]  # copy current list
        temp.append(data)
        # Simulate a tiny delay that increases the chance of a race
        time.sleep(0.001)
        shared_list[:] = temp  # write back to shared_list

    for src in sources:
        t = threading.Thread(target=worker, args=(src,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Shared list:", shared_list)


# Adding a lock to fix the race condition:
def lock_example():
    shared_list = []
    lock = threading.Lock()
    sources = ["url1", "url2", "url3", "url4"]
    threads = []

    def safe_worker(src):
        data = fetch_data(src)
        with lock:
            temp = shared_list[:]
            temp.append(data)
            time.sleep(0.001)
            shared_list[:] = temp

    for src in sources:
        t = threading.Thread(target=safe_worker, args=(src,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Shared list (with lock):", shared_list)


###############################################
###############################################
# 3
###############################################
###############################################
import queue

def producer_consumer_example():
    work_queue = queue.Queue()
    results = []
    lock = threading.Lock()

    # Producer: fetches data and puts it into the queue
    def producer(sources):
        for src in sources:
            data = fetch_data(src)
            work_queue.put(data)
        # Signal no more data
        for _ in range(num_consumers):
            work_queue.put(None)  # Sentinel values to signal end

    # Consumer: processes data from the queue
    def consumer():
        while True:
            data = work_queue.get()
            if data is None:
                work_queue.task_done()
                break
            processed = data.upper()  # simulate processing
            with lock:
                results.append(processed)
            work_queue.task_done()

    sources = ["url1", "url2", "url3", "url4", "url5"]
    num_consumers = 2

    prod_thread = threading.Thread(target=producer, args=(sources,))
    consumers = [threading.Thread(target=consumer) for _ in range(num_consumers)]

    # Start them
    prod_thread.start()
    for c in consumers:
        c.start()

    # Wait until the queue is fully processed
    prod_thread.join()
    work_queue.join()  # Wait for all tasks to be done

    print("Processed results:", results)

###############################################
###############################################
# 4
###############################################
###############################################

def event_condition_example():
    data_queue = queue.Queue()
    processing_done_event = threading.Event()
    condition = threading.Condition()
    processed_count = 0

    def producer(sources):
        for src in sources:
            data = fetch_data(src)
            data_queue.put(data)
        # Signal that no more items will be added
        processing_done_event.set()

    def consumer():
        nonlocal processed_count
        while True:
            try:
                data = data_queue.get(timeout=0.5)
            except queue.Empty:
                # If no data and event is set, we can stop
                if processing_done_event.is_set():
                    break
                continue
            # Process data
            processed = data.upper()
            with condition:
                processed_count += 1
                # Notify that new item has been processed
                condition.notify_all()
            data_queue.task_done()

    def reporter():
        # Wait for condition notifications
        while not processing_done_event.is_set() or not data_queue.empty():
            with condition:
                condition.wait(timeout=1.0)
                print(f"Reporter: {processed_count} items processed so far.")

    sources = ["url1", "url2", "url3", "url4", "url5"]
    prod_thread = threading.Thread(target=producer, args=(sources,))
    cons_thread = threading.Thread(target=consumer)
    rep_thread = threading.Thread(target=reporter)

    prod_thread.start()
    cons_thread.start()
    rep_thread.start()

    prod_thread.join()
    cons_thread.join()
    # Reporter may be waiting on condition, but once processing_done_event is set and queue empty, we can let it finish.
    # After consumer ends, we know no more processing will occur, so we can trigger reporter one last time.
    with condition:
        condition.notify_all()
    rep_thread.join()

    print("All done.")

###############################################
###############################################
# 5
###############################################
###############################################


def semaphore_example():
    semaphore = threading.Semaphore(2)  # Only two fetchers at a time
    sources = ["url1", "url2", "url3", "url4", "url5", "url6"]
    results = []
    lock = threading.Lock()

    def limited_fetch(src):
        with semaphore:
            # Only two threads run this section concurrently
            data = fetch_data(src)
            with lock:
                results.append(data)

    threads = [threading.Thread(target=limited_fetch, args=(s,)) for s in sources]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("Fetched with concurrency limit:", results)

###############################################
###############################################
# 6
###############################################
###############################################

def lifecycle_example():
    stop_event = threading.Event()
    sources = ["url1", "url2", "url3", "url4"]
    results = []
    lock = threading.Lock()

    def worker():
        while not stop_event.is_set():
            # Perform some periodic task
            with lock:
                print("Worker thread is running...")
            time.sleep(1)
        print("Worker thread shutting down...")

    # Daemon thread for background reporting
    def reporter():
        while not stop_event.is_set():
            with lock:
                print("Reporter checking in...")
            time.sleep(2)
        print("Reporter shutting down...")

    worker_thread = threading.Thread(target=worker)
    reporter_thread = threading.Thread(target=reporter, daemon=True)

    worker_thread.start()
    reporter_thread.start()

    # Let them run for a few seconds
    time.sleep(5)
    print("Main: Requesting shutdown.")
    stop_event.set()  # Signal threads to stop
    worker_thread.join()
    # Reporter is daemon, no need to join.

    print("Main thread exiting cleanly.")

###############################################
###############################################
# 7
###############################################
###############################################

def cpu_bound_task(n):
    # Simulate a CPU-intensive task
    total = 0
    for i in range(n):
        total += i**2
    return total

def performance_example():
    import time
    # Single-threaded CPU-bound
    start = time.time()
    for _ in range(5):
        cpu_bound_task(10_000_00)
    end = time.time()
    print("Single-threaded CPU-bound:", end - start, "seconds")

    # Multi-threaded CPU-bound
    start = time.time()
    threads = [threading.Thread(target=cpu_bound_task, args=(10_000_00,)) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    print("Multi-threaded CPU-bound:", end - start, "seconds")

    # Simulate I/O-bound tasks
    # Single-threaded I/O-bound
    def io_task():
        time.sleep(0.5)  # simulate network delay

    start = time.time()
    for _ in range(5):
        io_task()
    end = time.time()
    print("Single-threaded I/O-bound:", end - start, "seconds")

    # Multi-threaded I/O-bound
    start = time.time()
    threads = [threading.Thread(target=io_task) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    print("Multi-threaded I/O-bound:", end - start, "seconds")

if __name__ == "__main__":
    # basic_thread_example()
    race_condition_example()