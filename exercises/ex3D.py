import threading
import time
import random

class ConveyorBelt:
    def __init__(self, capacity):
        self.capacity = capacity
        self.belt = []  # Stores the parts on the conveyor belt
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    def produce(self, part, producer_name):
        with self.condition:
            while len(self.belt) >= self.capacity:
                self.condition.wait()  # Wait if the conveyor is full
            self.belt.append(part)
            print(f"{producer_name} produced {part}. Belt: {self.belt}")
            self.condition.notify_all()  # Notify consumers that a part is available

    def consume(self, consumer_name):
        with self.condition:
            while len(self.belt) == 0:
                self.condition.wait()  # Wait if the conveyor is empty
            part = self.belt.pop(0)  # Pick the first available part
            print(f"{consumer_name} consumed {part}. Belt: {self.belt}")
            self.condition.notify_all()  # Notify producers that space is available
            return part


class ProducerRobot(threading.Thread):
    def __init__(self, conveyor, name):
        super().__init__()
        self.conveyor = conveyor
        self.name = name

    def run(self):
        while True:
            part = random.choice(["A", "B"])  # Randomly produce part A or B
            time.sleep(random.uniform(0.5, 2))  # Simulate production time
            self.conveyor.produce(part, self.name)


class ConsumerRobot(threading.Thread):
    def __init__(self, conveyor, name):
        super().__init__()
        self.conveyor = conveyor
        self.name = name

    def run(self):
        while True:
            time.sleep(random.uniform(0.5, 2))  # Simulate time before consuming
            self.conveyor.consume(self.name)


if __name__ == "__main__":
    # Initialize the conveyor belt with a capacity of 3
    conveyor_belt = ConveyorBelt(capacity=3)

    # Create producer robots
    producer1 = ProducerRobot(conveyor_belt, "Producer1")
    producer2 = ProducerRobot(conveyor_belt, "Producer2")

    # Create consumer robots
    consumer1 = ConsumerRobot(conveyor_belt, "Consumer1")
    consumer2 = ConsumerRobot(conveyor_belt, "Consumer2")

    # Start all robots
    producer1.start()
    producer2.start()
    consumer1.start()
    consumer2.start()

    # Keep the main thread running to allow robot threads to work indefinitely
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping the simulation.")
