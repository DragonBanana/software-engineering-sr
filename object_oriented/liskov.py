# Exercise 9 - Liskov Substitution
class Payment:
    def process_payment(self, amount):
        raise NotImplementedError

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

if __name__ == '__main__':
    payments = [
        CreditCardPayment(),
        PayPalPayment()
    ]
    for payment in payments:
        payment.process_payment(100)
