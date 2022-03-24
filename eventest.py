import unittest
def check(x):
    if x%2==0:
        return "even"
    else:
        return "odd"
class Myapp(unittest.TestCase):
    def test_case_even(self):
        result = check(2)
        self.assertEqual("even",result)
    def test_case_even1(self):
        result = check(5)
        self.assertEqual("odd",result)

if __name__ == "__main__":
    unittest.main()