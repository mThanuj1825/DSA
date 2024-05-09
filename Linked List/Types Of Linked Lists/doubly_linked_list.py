class Node:
    def __init__(self, data: int, prev=None, nxt=None) -> None:
        self.data = data
        self.prev = prev
        self.next = nxt


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_front(self, data: int) -> None:
        if not self.head:
            self.head = self.tail = Node(data)
        else:
            new_node = Node(data, None, self.head)
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def add_back(self, data: int) -> None:
        if not self.head:
            self.head = self.tail = Node(data)
        else:
            new_node = Node(data, self.tail)
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def insert(self, data: int, index: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.add_front(data)
        elif index == self.size:
            self.add_back(data)
        else:
            halfway_index = self.size // 2

            if index < halfway_index:
                temp = self.head
                for _ in range(index - 1):
                    temp = temp.next

                new_node = Node(data, temp, temp.next)
                temp.next = new_node
                new_node.next.prev = new_node
            else:
                index = self.size - index + 1
                temp = self.tail
                for _ in range(index - 1):
                    temp = temp.prev

                new_node = Node(data, temp, temp.next)
                temp.next = new_node
                new_node.next.prev = new_node

            self.size += 1

    def delete(self, index: int) -> int | float:
        if index < 0 or index >= self.size:
            return float('inf')

        if index == 0:
            return self.pop_front()

        if index == self.size - 1:
            return self.pop_back()

        halfway_index = self.size // 2

        if index < halfway_index:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next

            data = temp.next.data
            temp.next = temp.next.next
            temp.next.prev = temp

            self.size -= 1
            return data
        else:
            index = self.size - index - 1
            temp = self.tail
            for _ in range(index - 1):
                temp = temp.prev

            data = temp.prev.data
            temp.prev = temp.prev.prev
            temp.prev.next = temp

            self.size -= 1
            return data

    def pop_front(self) -> int | float:
        if not self.head:
            return float('inf')

        data = self.head.data
        self.head.next.prev = None
        self.head = self.head.next
        self.size -= 1

        return data

    def pop_back(self) -> int | float:
        if not self.head:
            return float('inf')

        data = self.tail.data
        self.tail.prev.next = None
        self.tail = self.tail.prev
        self.size -= 1

        return data

    def print(self):
        temp = self.head
        print("None", end=" <-> ")
        while temp:
            print(temp.data, "<->", end=" ")
            temp = temp.next
        print("None")


l = LinkedList()
l.add_front(10)
l.print()

l.add_back(20)
l.add_back(30)
l.add_back(40)
l.print()

l.pop_front()
l.print()

l.pop_back()
l.print()

l.add_front(10)
l.add_back(50)
l.add_back(60)
l.add_back(70)
l.add_back(80)
l.print()

l.delete(2)
l.print()

l.insert(15, 1)
l.print()

l.insert(65, 5)
l.print()
