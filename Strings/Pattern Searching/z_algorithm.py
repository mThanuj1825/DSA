def solve(string: str, pattern: str) -> list[int]:
    indices = []

    def construct_z_array() -> list[int]:
        new_string = pattern + '$' + string
        z_array = [0]
        iterations = 0

        left, right = 0, 1
        while right < len(new_string):
            length = 0
            cur = right
            while right < len(new_string) and new_string[left] == new_string[right]:
                iterations += 1
                right += 1
                left += 1
                length += 1

            right = cur + 1
            left = 0
            z_array.append(length)

        print(iterations)

        return z_array

    z_array = construct_z_array()

    for i, n in enumerate(z_array):
        if n == len(pattern):
            indices.append(i - len(pattern) - 1)

    return indices


if __name__ == "__main__":
    string = "AABABA"
    pattern = "ABA"

    print(solve(string, pattern))
