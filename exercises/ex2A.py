from abc import ABC, abstractmethod

# Abstract base class for a sandwich
class Sandwich(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


# Concrete implementation for base sandwich types
class WhiteBread(Sandwich):
    def get_description(self):
        return "White Bread"

    def get_cost(self):
        return 2.0  # Base cost for white bread


class PitaBread(Sandwich):
    def get_description(self):
        return "Pita Bread"

    def get_cost(self):
        return 2.5  # Base cost for pita bread


class MultigrainBread(Sandwich):
    def get_description(self):
        return "Multigrain Bread"

    def get_cost(self):
        return 3.0  # Base cost for multigrain bread


# Abstract Decorator for ingredients
class IngredientDecorator(Sandwich):
    def __init__(self, sandwich):
        self._sandwich = sandwich

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


# Concrete Decorators for each ingredient
class Prosciutto(IngredientDecorator):
    def get_description(self):
        return self._sandwich.get_description() + ", Prosciutto"

    def get_cost(self):
        return self._sandwich.get_cost() + 1.5


class CookedHam(IngredientDecorator):
    def get_description(self):
        return self._sandwich.get_description() + ", Cooked Ham"

    def get_cost(self):
        return self._sandwich.get_cost() + 1.0


class Salami(IngredientDecorator):
    def get_description(self):
        return self._sandwich.get_description() + ", Salami"

    def get_cost(self):
        return self._sandwich.get_cost() + 1.2


class Tuna(IngredientDecorator):
    def get_description(self):
        return self._sandwich.get_description() + ", Tuna"

    def get_cost(self):
        return self._sandwich.get_cost() + 1.7


class Tomato(IngredientDecorator):
    def get_description(self):
        return self._sandwich.get_description() + ", Tomato"

    def get_cost(self):
        return self._sandwich.get_cost() + 0.5


class Mozzarella(IngredientDecorator):
    def get_description(self):
        return self._sandwich.get_description() + ", Mozzarella"

    def get_cost(self):
        return self._sandwich.get_cost() + 0.8


class Lettuce(IngredientDecorator):
    def get_description(self):
        return self._sandwich.get_description() + ", Lettuce"

    def get_cost(self):
        return self._sandwich.get_cost() + 0.3


class IcebergSalad(IngredientDecorator):
    def get_description(self):
        return self._sandwich.get_description() + ", Iceberg Salad"

    def get_cost(self):
        return self._sandwich.get_cost() + 0.4


class Capers(IngredientDecorator):
    def get_description(self):
        return self._sandwich.get_description() + ", Capers"

    def get_cost(self):
        return self._sandwich.get_cost() + 0.6


# Example usage
if __name__ == "__main__":
    # Start with a base sandwich
    sandwich = WhiteBread()

    # Add ingredients
    sandwich = Prosciutto(sandwich)
    sandwich = Tomato(sandwich)
    sandwich = Mozzarella(sandwich)

    # Display the final sandwich description and cost
    print("Sandwich Description:", sandwich.get_description())
    print("Total Cost: $", sandwich.get_cost())
