class Node:
    def __init__(self, data: int, cur_min: int | float, nxt=None):
        self.data = data
        self.cur_min = min(data, cur_min)
        self.next = nxt


class MinStack:
    def __init__(self):
        self.top = None
        self.cur_size = 0

    def push(self, data: int) -> None:
        new_node = Node(data, self.top.cur_min if self.top else float('inf'), self.top)
        self.top = new_node
        self.cur_size += 1

    def pop(self) -> int | float:
        if not self.is_empty():
            data = self.top.data
            self.top = self.top.bottom
            self.cur_size -= 1
            return data

        return float('-inf')

    def peek(self) -> int | float:
        if not self.is_empty():
            return self.top.data

        return float('-inf')

    def get_min(self) -> int | float:
        if not self.is_empty():
            return self.top.cur_min

        return float('-inf')

    def size(self) -> int:
        return self.cur_size

    def is_empty(self) -> bool:
        return self.top is None
