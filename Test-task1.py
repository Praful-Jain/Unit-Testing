import unittest
from Task1 import matches_played_peryear    # import function on which you have to perform unit testing

class TestClass(unittest.TestCase):

    # it will be called at the start of each test function ____ it will be common to all the test functions
    def setUp(self):
        self.expected_output = {'2017': 3, '2014': 2, '2015': 3, '2016': 2}
        self.output_received = matches_played_peryear()

    # test function ____ it's name should start with 'test'
    def test_matches_played_peryear(self):
        self.assertEqual(self.output_received, self.expected_output)        #cross checking the result


# if condition will check if the python scripts being run directly by itself 
if __name__ == "__main__":
    unittest.main()     # the test fun. will be executed only when you run script directly...not in another program
