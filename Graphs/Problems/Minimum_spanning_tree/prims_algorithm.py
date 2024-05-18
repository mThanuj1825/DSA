import heapq

from Graphs.Implementations.adjacency_matrix import Graph


def prims(g: Graph) -> Graph:
    heap = []
    heapq.heapify(heap)

    visited = set()
    minimum_spanning_tree = set()

    heapq.heappush(heap, (0, -1, 0))

    while len(visited) != g.nodes:
        cur = heapq.heappop(heap)
        if cur[2] not in visited:
            minimum_spanning_tree.add(cur)

            node = cur[2]
            visited.add(node)

            for i in range(g.nodes):
                if g.graph[node][i] != 0 and i not in visited:
                    heapq.heappush(heap, (g.graph[node][i], node, i))

    res_g = Graph(g.nodes)

    for weight, n1, n2 in minimum_spanning_tree:
        if n1 == -1:
            continue
        res_g.add_edge(n1, n2, weight)

    return res_g


if __name__ == '__main__':
    g = Graph(9)

    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)

    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)

    g.add_edge(2, 3, 7)
    g.add_edge(2, 5, 4)
    g.add_edge(2, 8, 2)

    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)

    g.add_edge(4, 5, 10)

    g.add_edge(5, 6, 2)

    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)

    g.add_edge(7, 8, 7)

    print(prims(g))
