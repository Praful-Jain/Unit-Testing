import unittest
from Task2 import matches_won_overyears

class TestClass(unittest.TestCase):
    
    def setUp(self):
        self.expected_output = {'Sunrisers Hyderabad': [0, 2, 1, 1], 'Delhi Daredevils': [1, 1, 1, 1], 
                            'Royal Challengers Bangalore': [1, 0, 0, 1]}
        self.output_received = matches_won_overyears()
        
    def test_matches_won_overyears(self):
        self.assertEqual(self.output_received,self.expected_output)
        
if __name__ == "__main__":
    unittest.main()