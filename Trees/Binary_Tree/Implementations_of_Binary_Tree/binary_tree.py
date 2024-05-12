class Node:
    def __init__(self, data: any, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None
        self.cur_size = 0

    def add(self, data: any) -> None:
        if self.root is None:
            self.root = Node(data)
            self.cur_size += 1
            return

        from Queues.Implementations_of_Queue.queue import Queue
        queue = Queue()
        queue.enqueue(self.root)

        while queue:
            current = queue.dequeue()
            if current.left is None:
                current.left = Node(data)
                self.cur_size += 1
                return
            elif current.right is None:
                current.right = Node(data)
                self.cur_size += 1
                return
            else:
                queue.enqueue(current.left)
                queue.enqueue(current.right)

    def remove(self, data: any) -> bool:
        def get_rightmost_leaf(node: Node) -> Node:
            current = node
            while current.right is not None:
                current = current.right
            return current

        def remove_node(node: Node, key: any) -> Node | None:
            if node is None:
                return None

            if node.data == key:
                if node.left is None and node.right is None:
                    return None
                elif node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    temp = get_rightmost_leaf(node.left)
                    node.data = temp.data
                    node.left = remove_node(node.left, temp.data)
            else:
                node.left = remove_node(node.left, key)
                node.right = remove_node(node.right, key)
            return node

        if not self.search(data):
            return False

        self.root = remove_node(self.root, data)
        self.cur_size -= 1
        return True

    def search(self, data: any) -> bool:
        if self.is_empty():
            return False

        def dfs(node: Node) -> bool:
            if node is None:
                return False

            if node.data == data:
                return True

            return dfs(node.left) or dfs(node.right)

        return dfs(self.root)

    def size(self) -> int:
        return self.cur_size

    def is_empty(self) -> bool:
        return self.root is None
