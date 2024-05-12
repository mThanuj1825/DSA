from Stacks.Implementations_of_Stack.stack import Stack


def solve(stk: Stack) -> None:
    def insert_bottom(data: any) -> None:
        if stk.is_empty():
            stk.push(data)
        else:
            cur = stk.pop()
            insert_bottom(data)
            stk.push(cur)

    if stk.is_empty():
        return

    cur = stk.pop()
    solve(stk)
    insert_bottom(cur)


if __name__ == '__main__':
    stk = Stack()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    stk.push(4)

    stk.print()

    solve(stk)

    stk.print()
