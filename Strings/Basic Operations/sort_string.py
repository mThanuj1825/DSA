def solve(string: str) -> str:
    freq_count = [0] * 256
    for c in string:
        freq_count[ord(c)] += 1

    res = ""
    for i, n in enumerate(freq_count):
        for j in range(n):
            res += chr(i)

    return res


if __name__ == "__main__":
    string = "thanuj"
    print(solve(string))
