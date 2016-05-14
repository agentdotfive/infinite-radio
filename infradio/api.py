
"""Infinite Radio API"""

import metagraph

import random
import uuid


class MetaStream:

    def __init__(self, server, stream_id):

        self.server = server
        self.stream_id = stream_id
        self.path = metagraph.MetaPath()
        self.position = -1

    def next(self):

        self.position = self.position + 1

        while self.position >= len(self.path.nodes):
            self.path.extend(self.server.graph, self.server.rng)

        return self.path.nodes[self.position]

    def prev(self):

        if self.position <= 0:
            return None

        self.position = self.position - 1

        return self.path.nodes[self.position]

    def get_history(self):

        return self.path.nodes


class MetaServer:

    def __init__(self, metagraph, seed):

        self.metagraph = metagraph
        self.rng = random.Random(seed)
        self.streams = {}

    def new_stream(self):

        stream = MetaStream(self, uuid.uuid4())
        self.streams[stream.stream_id] = stream
        return stream

    def get_stream(self, stream_id):

        return self.streams.get(stream_id, None)
