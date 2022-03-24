import unittest
def add(x,y):
    return x+y
class MyApp(unittest.TestCase):
    def test_case_add(self):
        a = 10
        b = 50
        c = add(a,b)
        self.assertEqual(c,a+b)
    def test_case_add1(self):
        a = 11.254
        b = 457.15
        c = add(a,b)
        self.assertEqual(c, a+b)

if __name__=="__main__":
    unittest.main()