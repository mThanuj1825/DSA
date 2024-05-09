from Linked_List.Types import singly_linked_list


def reverse(ll: singly_linked_list.LinkedList) -> None:
    prev, cur = None, ll.head

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    ll.head = prev


if __name__ == '__main__':
    ll = singly_linked_list.LinkedList()
    arr = [1, 2, 3, 4, 5]

    for i in arr:
        ll.add_back(i)

    reverse(ll)
    ll.print()
