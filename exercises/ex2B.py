import threading
import time
import random

class Pool:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.current_count = 0
        self.lock = threading.Lock()  # Ensures thread-safe access
        self.condition = threading.Condition(self.lock)  # Enables wait/notify mechanism
        self.current_type = None  # Tracks the current type of guests in the pool ('patients' or 'visitors')

    def enter_pool(self, guest_type, guest_name):
        with self.condition:
            while (
                self.current_count >= self.max_capacity  # Pool is full
                or (self.current_type is not None and self.current_type != guest_type)  # Other type is present
            ):
                self.condition.wait()  # Wait until conditions are satisfied

            # Add the guest to the pool
            self.current_count += 1
            self.current_type = guest_type
            print(f"{guest_name} ({guest_type}) entered the pool. Current count: {self.current_count}")

    def leave_pool(self, guest_name):
        with self.condition:
            self.current_count -= 1
            print(f"{guest_name} left the pool. Current count: {self.current_count}")

            # If the pool is empty, reset the type to allow the other type to enter
            if self.current_count == 0:
                self.current_type = None

            self.condition.notify_all()  # Notify all waiting threads


class Guest(threading.Thread):
    def __init__(self, pool, guest_type, guest_name):
        super().__init__()
        self.pool = pool
        self.guest_type = guest_type
        self.guest_name = guest_name

    def run(self):
        # Simulate a random delay before attempting to enter the pool
        time.sleep(random.uniform(0.1, 1.0))
        self.pool.enter_pool(self.guest_type, self.guest_name)

        # Simulate time spent in the pool
        time.sleep(random.uniform(0.5, 2.0))
        self.pool.leave_pool(self.guest_name)


if __name__ == "__main__":
    MAXP = 60  # Maximum pool capacity
    num_visitors = 50
    num_patients = 20

    pool = Pool(MAXP)

    guests = []

    # Create threads for patients
    for i in range(num_patients):
        patient = Guest(pool, "patient", f"Patient-{i + 1}")
        guests.append(patient)
        patient.start()

    # Create threads for visitors
    for i in range(num_visitors):
        visitor = Guest(pool, "visitor", f"Visitor-{i + 1}")
        guests.append(visitor)
        visitor.start()

    # Wait for all threads to finish
    for guest in guests:
        guest.join()

    print("Simulation complete.")
