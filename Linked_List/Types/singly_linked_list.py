class Node:
    def __init__(self, data: int, nxt=None) -> None:
        self.data = data
        self.next = nxt


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_front(self, data: int) -> None:
        if not self.head:
            self.head = Node(data)
        else:
            new_node = Node(data, self.head)
            self.head = new_node

        self.size += 1

    def add_back(self, data: int) -> None:
        if not self.head:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = Node(data)
        self.size += 1

    def insert(self, data: int, index: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.add_front(data)
        elif index == self.size:
            self.add_back(data)
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next

            new_node = Node(data, temp.next)
            temp.next = new_node

            self.size += 1

    def delete(self, index: int) -> int | float:
        if index < 0 or index >= self.size:
            return float('inf')

        if index == 0:
            return self.pop_front()

        if index == self.size - 1:
            return self.pop_back()

        temp = self.head
        for _ in range(index - 1):
            temp = temp.next

        data = temp.next.data
        temp.next = temp.next.next
        self.size -= 1

        return data

    def pop_front(self) -> int | float:
        if not self.head:
            return float('inf')

        data = self.head.data
        self.head = self.head.next
        self.size -= 1

        return data

    def pop_back(self) -> int | float:
        if not self.head:
            return float('inf')

        if not self.head.next:
            return self.pop_front()

        temp = self.head
        for _ in range(self.size - 2):
            temp = temp.next

        data = temp.next.data
        temp.next = None
        self.size -= 1

        return data

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, "->", end=" ")
            temp = temp.next
        print("None")


if __name__ == '__main__':
    l = LinkedList()
    l.add_front(10)
    l.add_back(20)
    l.add_back(30)
    l.add_back(40)
    l.add_back(50)
    l.print()

    l.delete(0)
    l.print()

    l.delete(3)
    l.print()

    l.delete(1)
    l.print()
