from abc import ABC, abstractmethod

# Strategy Interface
class TransportationStrategy(ABC):
    @abstractmethod
    def travel(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_time(self):
        pass

    @abstractmethod
    def get_comfort(self):
        pass


# Concrete Strategies
class Car(TransportationStrategy):
    def travel(self):
        return "Driving your own car to the airport."

    def get_cost(self):
        return 20  # Fuel cost

    def get_time(self):
        return 60  # Minutes

    def get_comfort(self):
        return "Medium"


class Taxi(TransportationStrategy):
    def travel(self):
        return "Taking a taxi to the airport."

    def get_cost(self):
        return 50  # Taxi fare

    def get_time(self):
        return 45  # Minutes

    def get_comfort(self):
        return "High"


class Shuttle(TransportationStrategy):
    def travel(self):
        return "Using an airport shuttle service."

    def get_cost(self):
        return 15  # Shuttle ticket

    def get_time(self):
        return 90  # Minutes

    def get_comfort(self):
        return "Low"


class Bus(TransportationStrategy):
    def travel(self):
        return "Taking a bus to the airport."

    def get_cost(self):
        return 10  # Bus ticket

    def get_time(self):
        return 120  # Minutes

    def get_comfort(self):
        return "Low"


class Limousine(TransportationStrategy):
    def travel(self):
        return "Using a limousine service to the airport."

    def get_cost(self):
        return 100  # Limousine fare

    def get_time(self):
        return 40  # Minutes

    def get_comfort(self):
        return "Very High"


class Subway(TransportationStrategy):
    def travel(self):
        return "Taking the subway to the airport."

    def get_cost(self):
        return 5  # Subway fare

    def get_time(self):
        return 70  # Minutes

    def get_comfort(self):
        return "Medium"


class Helicopter(TransportationStrategy):
    def travel(self):
        return "Flying to the airport by helicopter."

    def get_cost(self):
        return 200  # Helicopter fare

    def get_time(self):
        return 15  # Minutes

    def get_comfort(self):
        return "Very High"


# Context Class
class Person:
    def __init__(self, name):
        self.name = name
        self.strategy = None

    def set_strategy(self, strategy: TransportationStrategy):
        self.strategy = strategy

    def travel_to_airport(self):
        if not self.strategy:
            return f"{self.name} has not selected a mode of transportation."
        return (
            f"{self.name} is traveling to the airport.\n"
            f"Mode: {self.strategy.travel()}\n"
            f"Cost: ${self.strategy.get_cost()}\n"
            f"Time: {self.strategy.get_time()} minutes\n"
            f"Comfort: {self.strategy.get_comfort()}\n"
        )


# Example Usage
if __name__ == "__main__":
    john = Person("John")

    # Use different transportation strategies
    john.set_strategy(Car())
    print(john.travel_to_airport())

    john.set_strategy(Taxi())
    print(john.travel_to_airport())

    john.set_strategy(Helicopter())
    print(john.travel_to_airport())
