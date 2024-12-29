import threading
import time
import random


class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_cars = 0
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    def try_to_park(self, car_name):
        with self.condition:
            if self.current_cars >= self.capacity:
                print(f"{car_name}: Parking lot is full. Waiting to retry...")
                return False  # Cannot park
            self.current_cars += 1
            print(f"{car_name}: Parked. Spaces occupied: {self.current_cars}/{self.capacity}")
            return True  # Successfully parked

    def leave_parking(self, car_name):
        with self.condition:
            self.current_cars -= 1
            print(f"{car_name}: Left the parking lot. Spaces occupied: {self.current_cars}/{self.capacity}")
            self.condition.notify_all()  # Notify other cars that a space is available


class Car(threading.Thread):
    def __init__(self, parking_lot, car_name):
        super().__init__()
        self.parking_lot = parking_lot
        self.car_name = car_name

    def run(self):
        while True:
            # Attempt to park
            parked = self.parking_lot.try_to_park(self.car_name)
            if parked:
                # Stay parked for a random time (up to 20 minutes simulated as seconds)
                stay_time = random.uniform(5, 20)  # Simulating minutes as seconds
                print(f"{self.car_name}: Staying parked for {stay_time:.2f} seconds.")
                time.sleep(stay_time)

                # Leave the parking lot
                self.parking_lot.leave_parking(self.car_name)
                break
            else:
                # Wait 5 minutes (simulated as seconds) before retrying
                time.sleep(5)


if __name__ == "__main__":
    # Initialize the parking lot with a capacity of 5 spaces
    parking_lot = ParkingLot(capacity=5)

    # Create 10 car threads
    cars = [Car(parking_lot, f"Car-{i+1}") for i in range(10)]

    # Start all car threads
    for car in cars:
        car.start()

    # Wait for all cars to finish
    for car in cars:
        car.join()

    print("Simulation complete.")
