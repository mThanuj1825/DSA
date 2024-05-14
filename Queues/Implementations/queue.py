class Node:
    def __init__(self, data: any, prev=None):
        self.data = data
        self.prev = prev


class Queue:
    def __init__(self):
        self.front_pointer = self.rear_pointer = None
        self.cur_size = 0

    def enqueue(self, data: any) -> None:
        if self.is_empty():
            self.front_pointer = self.rear_pointer = Node(data)
        else:
            new_node = Node(data)
            self.rear_pointer.prev = new_node
            self.rear_pointer = new_node

        self.cur_size += 1

    def dequeue(self) -> any:
        if self.is_empty():
            return float('inf')

        data = self.front_pointer.data
        self.front_pointer = self.front_pointer.prev

        self.cur_size -= 1

        return data

    def front(self) -> any:
        if self.is_empty():
            return float('inf')

        return self.front_pointer.data

    def rear(self) -> any:
        if self.is_empty():
            return float('inf')

        return self.rear_pointer.data

    def is_empty(self) -> bool:
        return self.front_pointer is None

    def size(self) -> int:
        return self.cur_size


if __name__ == '__main__':
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    print(q.front())
    print(q.rear())

    for i in range(4):
        print(q.dequeue())

    print(q.size())
