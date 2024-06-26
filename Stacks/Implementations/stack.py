class Node:
    def __init__(self, data: int, bottom=None):
        self.data = data
        self.bottom = bottom


class Stack:
    def __init__(self):
        self.top = None
        self.cur_size = 0

    def push(self, data: any) -> None:
        new_node = Node(data, self.top)
        self.top = new_node
        self.cur_size += 1

    def pop(self) -> any:
        if not self.is_empty():
            data = self.top.data
            self.top = self.top.bottom
            self.cur_size -= 1
            return data

        return float('inf')

    def peek(self) -> any:
        if not self.is_empty():
            return self.top.data

        return float('inf')

    def size(self) -> int:
        return self.cur_size

    def is_empty(self) -> bool:
        return self.top is None

    def print(self) -> None:
        temp = self.top

        while temp:
            print(temp.data, " -> ", end=" ")
            temp = temp.bottom

        print("None")
