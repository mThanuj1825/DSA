from Graphs.Implementations.adjacency_list import Graph
from Stacks.Implementations.stack import Stack


def dfs(graph: Graph, src: int) -> str:
    if not graph.has_node(src):
        return "Node not present"

    content = ""
    visited = set()
    stk = Stack()

    stk.push(src)

    while not stk.is_empty():
        cur = stk.pop()
        if cur not in visited:
            visited.add(cur)
            content += str(cur) + ' -> '
            for child in g.graph[cur]:
                stk.push(child)

    return content[:-3]


if __name__ == '__main__':
    g = Graph()
    g.add_node(0)
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 0)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 0)
    g.add_edge(2, 1)
    g.add_edge(2, 4)
    g.add_edge(3, 1)
    g.add_edge(3, 4)
    g.add_edge(4, 2)
    g.add_edge(4, 3)

    print(g)

    print(dfs(g, 0))
