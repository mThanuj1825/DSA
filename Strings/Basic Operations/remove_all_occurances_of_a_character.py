def solve(string: str, character: str) -> str:
    res = ""
    for c in string:
        if c != character:
            res += c

    return res


if __name__ == "__main__":
    string = "hello world"
    character = "l"
    print(solve(string, character))
