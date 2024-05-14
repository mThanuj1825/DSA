import random

from methodtime import timeit

from Graphs.Implementations.adjacency_list import Graph


@timeit
def solve_dfs(g: Graph) -> bool:
    visited_nodes = set()

    def dfs(cur_node: int, visited: set[int], path: set[int]) -> bool:
        visited_nodes.add(cur_node)
        visited.add(cur_node)
        path.add(cur_node)

        for node in g.graph[cur_node]:
            if node in path:
                return True
            if node not in visited:
                if dfs(node, visited, path):
                    return True

        path.remove(cur_node)
        return False

    for node in g.present_nodes:
        if node not in visited_nodes and dfs(node, set(), set()):
            return True

    return False


def generate_large_random_graph(num_nodes: int, num_edges: int) -> Graph:
    g = Graph()

    for _ in range(num_edges):
        node1 = random.randint(0, num_nodes - 1)
        node2 = random.randint(0, num_nodes - 1)
        g.add_edge(node1, node2)

    return g


if __name__ == '__main__':
    g = generate_large_random_graph(1000, 10000)
    print(g)
    print(solve_dfs(g))
