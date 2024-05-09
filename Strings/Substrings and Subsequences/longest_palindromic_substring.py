def solve(string: str) -> str:
    start = 0
    end = 1
    for i in range(len(string)):
        l, r = i - 1, i
        while l > -1 and r < len(string) and string[l] == string[r]:
            if r - l + 1 > end:
                start = l
                end = r - l + 1

            l -= 1
            r += 1

        l, r = i - 1, i + 1
        while l > -1 and r < len(string) and string[l] == string[r]:
            if r - l + 1 > end:
                start = l
                end = r - l + 1

            l -= 1
            r += 1

    return string[start:start + end]


if __name__ == "__main__":
    string = "ababa"
    print(solve(string))
