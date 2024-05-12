class Node:
    def __init__(self, data: int, bottom=None):
        self.data = data
        self.bottom = bottom


class Stack:
    def __init__(self):
        self.top = None
        self.cur_size = 0

    def push(self, data: int) -> None:
        new_node = Node(data, self.top)
        self.top = new_node
        self.cur_size += 1

    def pop(self) -> int | float:
        if not self.is_empty():
            data = self.top.data
            self.top = self.top.bottom
            self.cur_size -= 1
            return data

        return float('inf')

    def peek(self) -> int | float:
        if not self.is_empty():
            return self.top.data

        return float('inf')

    def size(self) -> int:
        return self.cur_size

    def is_empty(self) -> bool:
        return self.top is None
