# Exercise 8 - Open/Closed
from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply_discount(self, amount):
        pass

class StudentDiscount(Discount):
    def apply_discount(self, amount):
        return amount * 0.9

class SeniorDiscount(Discount):
    def apply_discount(self, amount):
        return amount * 0.8

class RegularDiscount(Discount):
    def apply_discount(self, amount):
        return amount

def calculate_price(discount: Discount, amount):
    return discount.apply_discount(amount)

if __name__ == '__main__':
    student_discount = StudentDiscount()
    senior_discount = SeniorDiscount()
    regular_discount = RegularDiscount()

    print("Student Discount:", calculate_price(student_discount, 100))  # 90
    print("Senior Discount:", calculate_price(senior_discount, 100))  # 80
    print("Regular Discount:", calculate_price(regular_discount, 100))  # 100
