
"""Metadata Server and Streams"""

import random
import uuid

class MetaGraph:

    def __init__(self):
        pass

    def select_node(self, rng):
        pass

    def select_next_node(self, node, rng):
        pass


class MetaStream:

    def __init__(self, stream_id):
        self.stream_id = stream_id

    def  

def MetaServer:

    def __init__(self, metagraph, seed):
        
        self.metagraph = metagraph
        self.streams = []
        self.rng = random.Random(seed)

    def new_stream():
        
