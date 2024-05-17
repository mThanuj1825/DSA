from methodtime import timeit

from Graphs.Implementations.adjacency_matrix import Graph


@timeit
def floyd_warshall(graph: list[list[int]]) -> list[list[int]]:
    nodes = len(graph)
    prev = graph

    for mat in range(nodes):
        cur = []

        for i in range(nodes):
            row = []
            for j in range(nodes):
                if i == mat or j == mat or i == j:
                    row.append(prev[i][j])
                else:
                    row.append(min(prev[i][j], prev[i][mat] + prev[mat][j]))
            cur.append(row)
        prev = cur

    return prev


if __name__ == '__main__':
    g = Graph(4)

    g.add_edge(0, 1, 3, False)
    g.add_edge(0, 3, 7, False)
    g.add_edge(1, 0, 8, False)
    g.add_edge(1, 2, 2, False)
    g.add_edge(2, 0, 5, False)
    g.add_edge(2, 3, 1, False)
    g.add_edge(3, 0, 2, False)

    print(floyd_warshall(g.floyd_warshall_matrix()))
