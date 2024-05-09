def solve(string: str, pattern: str) -> list[int]:
    indices = []
    longest_prefix_suffix = [0] * len(pattern)

    prev_lps, i = 0, 1
    while i < len(pattern):
        if pattern[i] == pattern[prev_lps]:
            longest_prefix_suffix[i] = prev_lps + 1
            prev_lps += 1
            i += 1
        else:
            if prev_lps == 0:
                longest_prefix_suffix[i] = 0
                i += 1
            else:
                prev_lps = longest_prefix_suffix[prev_lps - 1]

    i = j = 0
    while i < len(string):
        if string[i] == pattern[j]:
            i, j = i + 1, j + 1
        else:
            if j == 0:
                i += 1
            else:
                j = longest_prefix_suffix[j - 1]

        if j == len(pattern):
            j = longest_prefix_suffix[j - 1]
            indices.append(i - len(pattern))

    return indices


if __name__ == "__main__":
    string = "AABABA"
    pattern = "ABA"

    print(solve(string, pattern))
