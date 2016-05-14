
"""Metadata Graph"""


class MetaGraph:

    def __init__(self):
        pass

    def select_node(self, rng):
        pass

    def select_next_node(self, node, rng):
        pass


class MetaPath:

    def __init__(self):

        self.nodes = []

    def extend(self, graph, rng):

        if not self.nodes:
            self.nodes.append(graph.select_node(rng))
        else:
            self.nodes.append(graph.select_next_node(self.nodes[-1], rng))

        return self.nodes[-1]

    def get_last_n(self, n):

        return self.nodes[-n:]
