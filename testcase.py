import unittest
class MyApp(unittest.TestCase):
    def test_case1(self):
        self.assertEqual("hello","hello")
    def test_case2(self):
        a=10
        b=12
        c = a+b
        self.assertEqual(a+b,c)

class MyApp2(unittest.TestCase):
    def test_case3(self):
        self.assertNotEqual("hello","hai")

if __name__ == "__main__":
    unittest.main()