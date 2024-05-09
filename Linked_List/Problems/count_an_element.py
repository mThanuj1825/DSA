from Linked_List.Types import singly_linked_list


def count(ll: singly_linked_list.LinkedList, element: int) -> int:
    temp = ll.head
    c = 0
    while temp:
        if temp.data == element:
            c += 1
        temp = temp.next

    return c


if __name__ == '__main__':
    ll = singly_linked_list.LinkedList()
    arr = [1, 2, 3, 4, 5, 3, 3]
    element = 3

    for i in arr:
        ll.add_back(i)

    print(count(ll, element))
