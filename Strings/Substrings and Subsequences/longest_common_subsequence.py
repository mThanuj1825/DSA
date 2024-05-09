def solve(string1: str, string2: str) -> int:
    n1, n2 = len(string1), len(string2)
    m = {}

    def lcs(i: int, j: int) -> int:
        nonlocal n1, n2, m
        key = (i << 16) | j

        if key in m:
            return m[key]

        if i == n1 or j == n2:
            m[key] = 0
            return 0

        if string1[i] == string2[j]:
            m[key] = 1 + lcs(i + 1, j + 1)
            return m[key]

        m[key] = max(lcs(i + 1, j), lcs(i, j + 1))
        return m[key]

    return lcs(0, 0)


if __name__ == "__main__":
    string1 = "abdace"
    string2 = "babce"

    print(solve(string1, string2))
