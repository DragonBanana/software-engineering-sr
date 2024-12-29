def foo(x, y):
    z = 0
    if (x > 0) and (y > 0):
        z = x
    return z



# Start
#   |
#   v
# z = 0
#   |
#   v
# z > 0 or y > 0? -----> No -----> Return z
#         |
#         v
#       z = x
#         |
#         v
#      Return z

import unittest
class TestFooFunction(unittest.TestCase):
    def test_statement_coverage(self):
        self.assertEqual(foo(1, 1), 1)  # True branch
        self.assertEqual(foo(-1, 1), 0)  # False branch

    def test_decision_coverage(self):
        self.assertEqual(foo(1, 1), 1)  # True branch
        self.assertEqual(foo(1, -1), 0)  # False branch

    def test_condition_coverage(self):
        self.assertEqual(foo(1, 1), 1)  # x > 0 and y > 0 are both true
        self.assertEqual(foo(-1, 1), 0)  # x > 0 is false, y > 0 is true
        self.assertEqual(foo(1, -1), 0)  # x > 0 is true, y > 0 is false

    def test_modified_condition(self):
        self.assertEqual(foo(0, 1), 0)  # With (z > 0) || (y > 0), y > 0 is true
        self.assertEqual(foo(0, -1), 0)  # With (z > 0) || (y > 0), both are false

if __name__ == "__main__":
    unittest.main()
