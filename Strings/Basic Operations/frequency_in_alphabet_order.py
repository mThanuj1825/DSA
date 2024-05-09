def solve(string: str) -> str:
    alpha = [0] * 26
    res = ""

    for c in string:
        if c.isalpha():
            alpha[ord(c) - ord('a')] += 1

    for i, n in enumerate(alpha):
        if n != 0:
            res += str(chr(ord('a') + i)) + str(n)

    return res


if __name__ == "__main__":
    string = "aabccccddd"
    print(solve(string))
