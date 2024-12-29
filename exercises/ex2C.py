def foo(a, d1, d2):
    if d1 > 0 and d2 <= d1:
        for i in range(d2 + 1):
            if a[i] > 0:
                print(a[i])
            if a[i] < 0:
                print(-a[i])
    print("End")

# Start
#   |
#   v
# d1 > 0 and d2 <= d1? -----> No -----> Print "End"
#         |
#         v
#   Loop: i = 0 to d2
#         |
#         v
#    a[i] > 0? -------> No -----> a[i] < 0? -------> No -----> Next iteration
#         |                        |
#         v                        v
#   Print a[i]               Print -a[i]
#         |
#         v
#   Next iteration
#         |
#         v
# Print "End"

import unittest
class TestFooFunction(unittest.TestCase):

    def test_valid_input(self):
        # Valid input, positive and negative numbers
        with self.assertLogs() as log:
            foo([1, -2, 3], 3, 2)
            self.assertIn("1", log.output[0])
            self.assertIn("2", log.output[1])
            self.assertIn("3", log.output[2])

    def test_d2_greater_than_d1(self):
        # d2 > d1, should cause IndexError
        with self.assertRaises(IndexError):
            foo([1, -2], 2, 3)

    def test_d1_less_than_or_equal_to_zero(self):
        # d1 <= 0, should skip loop and print "End"
        with self.assertLogs() as log:
            foo([1, -2, 3], -1, 2)
            self.assertIn("End", log.output[0])

    def test_invalid_d2(self):
        # d2 <= 0, should skip loop and print "End"
        with self.assertLogs() as log:
            foo([1, -2, 3], 3, -1)
            self.assertIn("End", log.output[0])

    def test_empty_array(self):
        # Empty array, should print "End"
        with self.assertLogs() as log:
            foo([], 0, 0)
            self.assertIn("End", log.output[0])

    def test_only_positive_numbers(self):
        # Array with only positive numbers
        with self.assertLogs() as log:
            foo([2, 3, 4], 3, 2)
            self.assertIn("2", log.output[0])
            self.assertIn("3", log.output[1])
            self.assertIn("4", log.output[2])

    def test_only_negative_numbers(self):
        # Array with only negative numbers
        with self.assertLogs() as log:
            foo([-1, -2, -3], 3, 2)
            self.assertIn("1", log.output[0])
            self.assertIn("2", log.output[1])
            self.assertIn("3", log.output[2])

if __name__ == "__main__":
    unittest.main()

