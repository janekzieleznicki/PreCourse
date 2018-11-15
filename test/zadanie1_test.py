import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
# from test import support
from parameterized import parameterized
from src import zadanie1

class Zadanie1Test(unittest.TestCase):

    def setUp(self):
        # print(os.getcwd())
        # with open('./tests/rows.txt', 'rt') as csvfile:
        self.table = zadanie1.Table()

    @parameterized.expand([
        [[5, 1, 9, 5], 8],
        [[7, 5, 3], 4],
        [[2, 4, 6, 8], 6]
    ])
    def test_row(self, data, result):
        self.assertEqual(
        self.table.calc_row(data), 
        result)
    
    def test_sheet(self):
        self.assertEqual(
            self.table.calc_sheet(
                [[5, 1, 9, 5],
                [7, 5, 3],
                [2, 4, 6, 8]]
            ),
            18
        )
    
    def test_loaded_data(self):
        self.assertEqual(
            self.table.control_sum(), 18
        )

if __name__ == '__main__':
    unittest.main()