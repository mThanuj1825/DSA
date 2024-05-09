from Linked_List.Types import singly_linked_list


def solve(head: singly_linked_list.Node, target: int) -> int:
    temp = head
    idx = 0
    while temp and temp.data != target:
        idx += 1
        temp = temp.next

    return idx if temp else -1


if __name__ == '__main__':
    ll = singly_linked_list.LinkedList()
    arr = [1, 7, 4, 5, 3, 9, 0, 2, 4]
    target = 3

    for i in arr:
        ll.add_back(i)

    print(solve(ll.head, target))
