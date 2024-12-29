# Define a base billing strategy
class BillingStrategy:
    def calculate_bill(self, base_charge):
        raise NotImplementedError("Subclasses must implement this method")


# Concrete billing strategies
class InsuredBillingStrategy(BillingStrategy):
    def calculate_bill(self, base_charge):
        return base_charge * 0.8  # 20% discount


class UninsuredBillingStrategy(BillingStrategy):
    def calculate_bill(self, base_charge):
        return base_charge


class GovernmentBillingStrategy(BillingStrategy):
    def calculate_bill(self, base_charge):
        return base_charge * 0.5  # 50% discount


# Context class that uses the strategy
class BillingSystem:
    def __init__(self, strategy: BillingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: BillingStrategy):
        self.strategy = strategy

    def calculate_bill(self, base_charge):
        return self.strategy.calculate_bill(base_charge)


# Client code
insured_strategy = InsuredBillingStrategy()
uninsured_strategy = UninsuredBillingStrategy()
government_strategy = GovernmentBillingStrategy()

billing_system = BillingSystem(insured_strategy)
print(billing_system.calculate_bill(1000))  # Output: 800

billing_system.set_strategy(uninsured_strategy)
print(billing_system.calculate_bill(1000))  # Output: 1000

billing_system.set_strategy(government_strategy)
print(billing_system.calculate_bill(1000))  # Output: 500
