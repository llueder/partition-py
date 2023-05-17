import networkx as nx
import heapq

from .types import Instance, Partition

class _Node:
    def __init__(self, idx, number) -> None:
        self.idx = idx
        self.number = number
        self.value = self.number
        self.color = None

    def __lt__(self, o) -> bool:
        return self.value > o.value  # yes, its reversed, to have a reversed heap

def _color_tree(g):
    start_node = list(g.nodes)[0]
    start_node.color = 0

    for n in nx.dfs_preorder_nodes(g, source=start_node):
        if n.color is None:
            for nn in g.neighbors(n):
                if nn.color is not None:
                    n.color = 1 - nn.color
                    break

def karmarkar_karp(numbers : Instance, return_indices=False) -> Partition:
    if len(numbers) < 2:
        raise ValueError("PARTITION instance must contain at least 2 numbers")

    g = nx.Graph()
    for idx, number in enumerate(numbers):
        node = _Node(idx, number)
        g.add_node(node)

    active_nodes_sorted = list(g.nodes)
    heapq.heapify(active_nodes_sorted)

    while len(active_nodes_sorted) > 1:
        larger = heapq.heappop(active_nodes_sorted)
        smaller = heapq.heappop(active_nodes_sorted)
        larger.value = larger.value - smaller.value
        heapq.heappush(active_nodes_sorted, larger)
        g.add_edge(larger, smaller)

    _color_tree(g)
    list_a = [n.number if not return_indices else n.idx for n in g.nodes if n.color == 0]
    list_b = [n.number if not return_indices else n.idx for n in g.nodes if n.color == 1]

    return (list_a, list_b)
