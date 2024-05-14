from Stacks.Implementations.stack import Stack


def solve(brackets: str) -> bool:
    mp = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    stk = Stack()

    for bracket in brackets:
        if bracket in mp:
            if stk.is_empty():
                return False

            if mp[bracket] != stk.pop():
                return False
        else:
            stk.push(bracket)

    return True


if __name__ == '__main__':
    brackets = "[()]{}{[()()]()}"

    print(solve(brackets))
