from Stack.stack import Stack


class Queue:
    def __init__(self):
        self.stk1 = Stack()
        self.stk2 = Stack()

    def enqueue(self, data) -> None:
        self.stk1.push(data)

    def dequeue(self) -> int | float:
        if self.is_empty():
            return float('inf')

        if self.stk2.is_empty():
            while not self.stk1.is_empty():
                self.stk2.push(self.stk1.pop())

        return self.stk2.pop()

    def is_empty(self) -> bool:
        return self.stk1.is_empty() and self.stk2.is_empty()

    def size(self) -> int:
        return self.stk1.size() + self.stk2.size()
