from Stacks.Implementations_of_Stack import stack


def solve(arr: list[int]) -> list[int]:
    stk = stack.Stack()
    res = [-1] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        stk.print()
        while not stk.is_empty() and stk.peek() <= arr[i]:
            stk.pop()

        if stk.is_empty():
            res[i] = -1
        else:
            res[i] = stk.peek()

        stk.push(arr[i])

    return res


if __name__ == '__main__':
    arr = [13, 7, 6, 12]

    print(solve(arr.copy()))
