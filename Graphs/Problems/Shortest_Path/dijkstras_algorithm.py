import sys

from Graphs.Implementations.adjacency_matrix import Graph


def dijkstras(g: Graph, src: int) -> list[int]:
    distance_vector = [sys.maxsize] * g.nodes
    distance_vector[src] = 0
    shortest_path_tree = [False] * g.nodes

    def get_closest_node() -> int:
        min_distance = sys.maxsize
        closest_node = -1

        for node, distance in enumerate(distance_vector):
            if not shortest_path_tree[node] and distance < min_distance:
                min_distance = distance
                closest_node = node

        return closest_node

    for _ in range(g.nodes):
        current_closest_node = get_closest_node()
        shortest_path_tree[current_closest_node] = True

        for node in range(g.nodes):
            if not shortest_path_tree[node] and g.graph[current_closest_node][node] != 0:
                distance_vector[node] = min(distance_vector[node],
                                            distance_vector[current_closest_node] + g.graph[current_closest_node][node])

    return distance_vector


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
    g.add_edge(5, 3, 14)
    g.add_edge(5, 4, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(7, 8, 7)
    g.add_edge(7, 6, 1)
    g.add_edge(8, 6, 6)

    print(dijkstras(g, 0))
