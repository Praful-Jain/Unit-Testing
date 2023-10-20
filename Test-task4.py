import unittest
from Task4 import top_economical_bowlers

class TestClass(unittest.TestCase):
    def setUp(self) :
        self.expected_output = {'MG Johnson': 0.0, 'VR Aaron': 0.0, 'AN Ahmed': 0.0, 'AD Mathews': 2.4, 'UT Yadav': 4.5, 
                            'TA Boult': 9.0, 'MM Sharma': 12.0, 'A Nehra': 12.0, 'Karanveer Singh': 12.0, 'DJ Bravo': 12.0}
        self.output_received = top_economical_bowlers()
        
    def test_top_economical_bowlers(self):
        self.assertEqual(self.output_received,self.expected_output)
        
if __name__ == "__main__":
    unittest.main()