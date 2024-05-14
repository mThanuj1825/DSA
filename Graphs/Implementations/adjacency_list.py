class Graph:
    def __init__(self):
        self.graph = {}
        self.edges = 0
        self.present_nodes = set()

    def add_edge(self, src: int, dst: int) -> None:
        if src not in self.present_nodes:
            return

        self.graph[src].add(dst)
        self.edges += 1

    def remove_edge(self, src: int, dst: int) -> None:
        if src not in self.present_nodes:
            return

        self.graph[src].remove(dst)
        self.edges -= 1

    def add_node(self, node: int) -> None:
        if node in self.graph:
            return

        self.graph[node] = set()
        self.present_nodes.add(node)

    def remove_node(self, node: int) -> None:
        if node not in self.present_nodes:
            return

        for src in self.graph:
            if node in self.graph[src]:
                self.graph[src].remove(node)
                self.edges -= 1

        self.edges -= len(self.graph[node])
        self.graph.pop(node)
        self.present_nodes.remove(node)

    def has_node(self, node: int) -> bool:
        return node in self.present_nodes

    def total_edges(self) -> int:
        return self.edges

    def transpose(self) -> None:
        if not self.present_nodes:
            return

        cur_graph = {}

        for src, dst in self.graph.items():
            for d in dst:
                if d in cur_graph:
                    cur_graph[d].add(src)
                else:
                    cur_graph[d] = {src}

        self.graph = cur_graph

    def __repr__(self) -> str:
        content = ''
        for src, dst in self.graph.items():
            content += str(src) + ': ' + str(list(dst)) + '\n'

        return content[:-1]


if __name__ == '__main__':
    g = Graph()
    # g.add_node(1)
    # g.add_node(2)
    # # print(g)
    #
    # g.add_edge(1, 2)
    # # print(g)
    # g.add_node(3)
    # g.add_node(4)
    # g.add_node(5)
    # # print(g)
    #
    # g.add_edge(2, 4)
    # g.add_edge(3, 5)
    # g.add_edge(4, 5)
    # g.add_edge(5, 2)
    # g.add_edge(1, 3)
    # # print(g)
    #
    # # print(g)
    # # print(g.present_nodes)
    # g.remove_node(2)
    # # print(g)
    #
    # # print(g.present_nodes)
    #
    # g.remove_edge(1, 3)
    # # print(g)
    # # print(g.total_edges())

    g.add_node(0)
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)

    g.add_edge(0, 1)
    g.add_edge(0, 3)
    g.add_edge(0, 4)
    g.add_edge(2, 0)
    g.add_edge(3, 2)
    g.add_edge(4, 1)
    g.add_edge(4, 3)

    # print(g)

    g.transpose()

    print(g)
