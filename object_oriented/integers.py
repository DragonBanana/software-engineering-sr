# Exercise 5 - Array of Integers
class IntegerArray:
    def __init__(self, array):
        self.array = array

    def __add__(self, other):
        max_length = max(len(self.array), len(other.array))
        result = [(self.array[i] if i < len(self.array) else 0) +
                  (other.array[i] if i < len(other.array) else 0)
                  for i in range(max_length)]
        return IntegerArray(result)

    def __sub__(self, other):
        max_length = max(len(self.array), len(other.array))
        result = [(self.array[i] if i < len(self.array) else 0) -
                  (other.array[i] if i < len(other.array) else 0)
                  for i in range(max_length)]
        return IntegerArray(result)

    def __repr__(self):
        return str(self.array)

if __name__ == '__main__':
    arr1 = IntegerArray([1, 2, 3])
    arr2 = IntegerArray([4, 5])
    print(arr1 + arr2)  # [5, 7, 3]
    print(arr1 - arr2)  # [-3, -3, 3]