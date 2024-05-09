def solve(string: str, pattern: str) -> list[int]:
    indices = []
    for i in range(len(string) - len(pattern) + 1):
        j = 0

        while j < len(pattern) and string[i + j] == pattern[j]:
            j += 1

        if j == len(pattern):
            indices.append(i)

    return indices


if __name__ == "__main__":
    string = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"

    print(solve(string, pattern))
