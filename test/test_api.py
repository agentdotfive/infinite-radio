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
        return (curr_path, index + 1, self.mock_paths[curr_path][index + 1])


class TestAPI(unittest.TestCase):

    def test_new_streams(self):

        metagraph = MockMetagraph([list(range(0, 10)),
                                   list(range(10, 20))])

        metaserver = infradio.MetaServer(metagraph, 0)
        stream_a = metaserver.new_stream()
        stream_b = metaserver.new_stream()

        for i in range(0, 10):
            _, _, j = stream_a.next()
            self.assertEqual(i, j)
            _, _, k = stream_b.next()
            self.assertEqual(i + 10, k)

        self.assertEqual([x for _, _, x in stream_a.get_history()],
                         list(range(0, 10)))
        self.assertEqual([x for _, _, x in stream_b.get_history()],
                         list(range(10, 20)))
