import unittest
from Task3 import extra_runs_2016

class TectClass(unittest.TestCase):
    def setUp(self):
        self.expected_output = {'Sunrisers Hyderabad': 43, 'Delhi Daredevils': 55}
        self.output_received = extra_runs_2016()
        
    def test_extra_runs_2016(self):
        self.assertEqual(self.output_received,self.expected_output)
        
if __name__ == "__main__":
    unittest.main()