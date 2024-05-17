import sys

from Graphs.Implementations.adjacency_matrix import Graph


def bellman_ford(g: Graph, src: int) -> list[int]:
    edges = []

    for node, neighbors in enumerate(g.graph):
        for neighbor, weight in enumerate(neighbors):
            if weight != 0:
                edges.append((node, neighbor))

    distance_vector = [sys.maxsize] * g.nodes
    distance_vector[src] = 0

    for _ in range(g.nodes - 1):
        count = 0
        for edge in edges:
            if distance_vector[edge[0]] + g.graph[edge[0]][edge[1]] < distance_vector[edge[1]]:
                count += 1
                distance_vector[edge[1]] = distance_vector[edge[0]] + g.graph[edge[0]][edge[1]]

        if count == 0:
            break

    return distance_vector


if __name__ == '__main__':
    g = Graph(7)

    g.add_edge(0, 1, 6, False)
    g.add_edge(0, 2, 5, False)
    g.add_edge(0, 3, 5, False)
    g.add_edge(1, 4, -1, False)
    g.add_edge(2, 1, -2, False)
    g.add_edge(2, 4, 1, False)
    g.add_edge(3, 2, -2, False)
    g.add_edge(3, 5, -1, False)
    g.add_edge(4, 6, 3, False)
    g.add_edge(5, 6, 3, False)

    print(bellman_ford(g, 0))
