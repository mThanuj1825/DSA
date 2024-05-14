from Stacks.Implementations.stack import Stack


def solve(string: str) -> str:
    res = ""
    stk = Stack()

    for character in string:
        if character == ' ':
            while not stk.is_empty():
                res += stk.pop()
            res += " "
        else:
            stk.push(character)

    while not stk.is_empty():
        res += stk.pop()

    return res


if __name__ == '__main__':
    string = "Hello World"
    print(solve(string))
