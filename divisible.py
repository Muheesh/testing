import unittest
def divisible7(x):
    if x%7==0:
        return True
    else:
        return False

class Myapp(unittest.TestCase):
    def test_case_divisible(self):
        result = divisible7(14)
        self.assertTrue(result)
    def test_case_divisible1(self):
        result = divisible7(13)
        self.assertFalse(result)
if __name__=="__main__":
    unittest.main()