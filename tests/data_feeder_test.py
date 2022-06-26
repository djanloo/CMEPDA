# Make possible importing modules from parent directory
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import unittest
from cloudatlas.utils import DataFeeder, animate_time_series

class dfTest(unittest.TestCase):

    def setUp(self):
        self. test_data = DataFeeder("splitted_dataset/test_splitted_data").feed()
        self.block = next(self.test_data)

    def test_order(self):
        # Check for bug #2
        # Since the order is toa, ts, outcome shapes must be
        self.assertEqual(self.block["toa"].shape[1:], (9,9,1))
        self.assertEqual(self.block["time_series"].shape[1:], (80,9,9))

    def test_anim(self):
        # Animation is not shown, only checks for errors
        u = animate_time_series(self.block["time_series"][0])
