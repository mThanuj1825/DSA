def solve(string: str) -> int:
    mp = {}

    def lps(i: int, j: int):
        key = (i << 16) | j
        if key in mp:
            return mp[key]

        if i == j:
            return 1

        if string[i] == string[j] and i + 1 == j:
            return 2

        if string[i] == string[j]:
            mp[key] = 2 + lps(i + 1, j - 1)
            return mp[key]

        mp[key] = max(lps(i + 1, j), lps(i, j - 1))
        return mp[key]

    return lps(0, len(string) - 1)


if __name__ == "__main__":
    string = "GEEKSFORGEEKS"
    print(solve(string))
