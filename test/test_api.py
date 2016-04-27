
"""Tests of the infinite radio API"""


import unittest
import infradio


class TestAPI(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(infradio.hello_world(), 0)
