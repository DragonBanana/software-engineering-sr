# Exercise 2 - Multiple Inheritance
class A:
    def say(self):
        return "A"

class B(A):
    def say(self):
        return "B"

class C(A):
    def say(self):
        return "C"

class D(B, C):
    pass

d = D()
print(d.say())  # Resolves to "B" because of method resolution order (MRO)







