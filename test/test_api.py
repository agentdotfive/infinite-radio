"""Tests of the infinite radio API"""

import unittest
import infradio


class MockMetagraph:

    def __init__(self, mock_paths):
        self.curr_path = 0
        self.mock_paths = mock_paths

    def select_node(self, rng):
        curr_path = self.curr_path
        self.curr_path = (self.curr_path + 1) % len(self.mock_paths)
        return self.select_next_node((curr_path, -1, None), rng)

    def select_next_node(self, node, rng):
        curr_path, index, _ = node
        return (curr_path, index + 1, self.mock_paths[index + 1])


class TestAPI(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(infradio.hello_world(), 0)

    def test_new_stream(self):

        # TODO: Turn back on
        if True:
            return

        metagraph = MockMetagraph([list(range(0, 10)),
                                   list(range(10, 20))])

        metaserver = infradio.create_metaserver(metagraph)
        metastream_a = metaserver.new_metastream()
        metastream_b = metaserver.new_metastream()

        for i in range(0, 10):
            _, _, j = metastream_a.next()
            self.assertEqual(i, j)
            _, _, k = metastream_b.next()
            self.assertEqual(i, k + 10)
