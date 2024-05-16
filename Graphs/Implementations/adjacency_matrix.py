class Graph:
    def __init__(self, nodes: int):
        self.nodes = nodes
        self.graph = [[0] * nodes for _ in range(nodes)]
        self.edges = 0
        self.present_nodes = set()

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        if src < 0 or src >= self.nodes or dst < 0 or dst >= self.nodes or self.graph[src][dst] != 0:
            return

        self.present_nodes.add(src)
        self.present_nodes.add(dst)
        self.graph[src][dst] = weight
        self.edges += 1

    def remove_edge(self, src: int, dst: int) -> None:
        if src < 0 or src >= self.nodes or dst < 0 or dst >= self.nodes or self.graph[src][dst] == 0:
            return

        self.graph[src][dst] = 0
        self.edges -= 1

    def remove_node(self, node: int) -> None:
        if node < 0 or node >= self.nodes:
            return

        for i in range(self.nodes):
            for j in range(self.nodes):
                if i == node or j == node and self.graph[i][j] != 0:
                    self.remove_edge(i, j)

        self.present_nodes.remove(node)

    def has_node(self, node: int) -> bool:
        return node in self.present_nodes

    def total_edges(self) -> int:
        return self.edges

    def __repr__(self) -> str:
        content = ''
        for row in self.graph:
            content += row.__repr__() + '\n'

        return content[:-1]


if __name__ == '__main__':
    g = Graph(3)

    g.add_edge(0, 1, 3)
    g.add_edge(1, 2)
    g.add_edge(2, 2)
    g.add_edge(2, 0)
    print(g)

    g.remove_node(2)
    print(g.has_node(1))
    print(g)
    print(g.has_node(2))
