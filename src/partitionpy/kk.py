"""
Karmarkar-Karp algorithm
"""
import heapq
import networkx as nx

from .types import Instance, Partition

class _Node:
    # pylint: disable=too-few-public-methods
    def __init__(self, idx, number) -> None:
        self.idx = idx
        self.number = number
        self.value = self.number
        self.color = None

    def __lt__(self, other) -> bool:
        return self.value > other.value  # yes, its reversed, to have a reversed heap

def _color_tree(tree):
    start_node = list(tree.nodes)[0]
    start_node.color = 0

    for node in nx.dfs_preorder_nodes(tree, source=start_node):
        if node.color is None:
            for neighbor in tree.neighbors(node):
                if neighbor.color is not None:
                    node.color = 1 - neighbor.color
                    break

def karmarkar_karp(numbers : Instance, return_indices=False) -> Partition:
    """
    State of the art approximation algorithm. Also known as largest differencing method (LDM).

    Runtime complexity in O(nlogn).
    Yields discrepancy in O(1/n^(0.72)) on average.

    References:
    N. Karmarkar and R. M. Karp. The differencing method of set partitioning. Technical
      Report UCB/CSD-83-113, EECS Department, University of California, Berkeley, 1983.
      URL http://www2.eecs.berkeley.edu/Pubs/TechRpts/1983/6353.html
    R. E. Korf. A complete anytime algorithm for number partitioning. Artif. Intell., 106
      (2):181–203, dec 1998. ISSN 0004-3702. doi: 10.1016/S0004-3702(98)00086-1. URL
      https://doi.org/10.1016/S0004-3702(98)00086-1
    (Korf is very readable.)

    :param: numbers is a list of integers.
    :param: return_indices can be set to true when the algorithm shall return the indices to build
            the partition instead of the partition itself

    Implementation notes:
    This implementation is not as fast and probably more memory consuming than the implementation
    from the numberpartitioning package (https://pypi.org/project/numberpartitioning/).
    Trading the quite readable implementation with a _Node class and using networkx against a more
    optimized version is advised.
    """
    if len(numbers) < 2:
        raise ValueError("PARTITION instance must contain at least 2 numbers")

    tree = nx.Graph()
    for idx, number in enumerate(numbers):
        node = _Node(idx, number)
        tree.add_node(node)

    active_nodes_sorted = list(tree.nodes)
    heapq.heapify(active_nodes_sorted)

    while len(active_nodes_sorted) > 1:
        larger = heapq.heappop(active_nodes_sorted)
        smaller = heapq.heappop(active_nodes_sorted)
        larger.value = larger.value - smaller.value
        heapq.heappush(active_nodes_sorted, larger)
        tree.add_edge(larger, smaller)

    _color_tree(tree)
    list_a = [node.idx if return_indices else node.number for node in tree.nodes if node.color==0]
    list_b = [node.idx if return_indices else node.number for node in tree.nodes if node.color==1]

    return (list_a, list_b)
