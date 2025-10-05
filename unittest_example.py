import unittest
from my_function import my_add

# define the unit tests
class my_unit_tests(unittest.TestCase):
    def test_add(self):
        
        # test adding integers
        self.assertEqual(my_add(2, 3), 5)

        # test adding negative integers
        self.assertEqual(my_add(-6, 3), -3)

        # test adding floats
        self.assertEqual(my_add(3.1, 5.4), 8.5)

# run the tests
if __name__ == "__main__":
    unittest.main()

 
    



