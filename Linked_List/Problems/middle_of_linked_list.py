from Linked_List.Types import singly_linked_list


def solve(ll: singly_linked_list.LinkedList) -> int:
    temp = ll.head

    for _ in range(ll.size // 2):
        temp = temp.next

    return temp.data


if __name__ == '__main__':
    ll = singly_linked_list.LinkedList()
    arr = [1, 2, 3, 4, 5]

    for i in arr:
        ll.add_back(i)

    print(solve(ll))
