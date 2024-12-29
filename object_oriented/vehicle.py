from abc import ABC, abstractmethod

# Abstract base class: Vehicle
class Vehicle(ABC):
    def __init__(self, make, model, year, engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine  # Composition: All vehicles have an engine

    @abstractmethod
    def max_speed(self):
        pass

    @abstractmethod
    def fuel_efficiency(self):
        pass

    def __repr__(self):
        return f"{self.year} {self.make} {self.model} (Engine: {self.engine})"


# Concrete class: Engine (used in composition)
class Engine:
    def __init__(self, horsepower, engine_type):
        self.horsepower = horsepower
        self.engine_type = engine_type

    def __repr__(self):
        return f"{self.horsepower} HP {self.engine_type} engine"


# Concrete class: Car
class Car(Vehicle):
    def __init__(self, make, model, year, seats, engine):
        super().__init__(make, model, year, engine)
        self.seats = seats

    def max_speed(self):
        return 200 + self.engine.horsepower * 0.1

    def fuel_efficiency(self):
        return 15 - self.engine.horsepower * 0.02

    def __repr__(self):
        return f"{super().__repr__()} (Seats: {self.seats})"


# Concrete class: Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type, engine):
        super().__init__(make, model, year, engine)
        self.type = type

    def max_speed(self):
        return 180 if self.type == "cruiser" else 220 + self.engine.horsepower * 0.05

    def fuel_efficiency(self):
        return 25 - self.engine.horsepower * 0.01

    def __repr__(self):
        return f"{super().__repr__()} (Type: {self.type})"


# Concrete class: Truck
class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity, engine):
        super().__init__(make, model, year, engine)
        self.cargo_capacity = cargo_capacity

    def max_speed(self):
        return 120 + self.engine.horsepower * 0.05

    def fuel_efficiency(self):
        return 8 - self.cargo_capacity * 0.5

    def __repr__(self):
        return f"{super().__repr__()} (Cargo Capacity: {self.cargo_capacity} tons)"


# Example usage
if __name__ == "__main__":
    # Create engines
    engine1 = Engine(150, "petrol")
    engine2 = Engine(80, "diesel")
    engine3 = Engine(500, "diesel")

    # Create vehicles
    car = Car("Toyota", "Corolla", 2020, 5, engine1)
    motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2019, "cruiser", engine2)
    truck = Truck("Volvo", "FH16", 2018, 10, engine3)

    # Display vehicles
    print(car)
    print(motorcycle)
    print(truck)
