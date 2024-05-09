def solve(string: str) -> list[str]:
    substrings = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substrings.append(string[i:j])

    return substrings


if __name__ == "__main__":
    string = "abcd"
    print(solve(string))
