def solve(string: str, pattern: str) -> list[int]:
    indices = []

    def construct_z_array() -> list[int]:
        new_string = pattern + '$' + string
        z_array = [0] * len(new_string)
        left, right = 0, 0

        for i in range(1, len(new_string)):
            if i > right:
                left = right = i
                while right < len(new_string) and new_string[right - left] == new_string[right]:
                    right += 1

                z_array[i] = right - left
                right -= 1
            else:
                k = i - left
                if z_array[k] < right - i + 1:
                    z_array[i] = z_array[k]
                else:
                    left = i
                    while right < len(new_string) and new_string[right - left] == new_string[right]:
                        right += 1

                    z_array[i] = right - left
                    right -= 1

        return z_array

    z_array = construct_z_array()

    for i, n in enumerate(z_array):
        if n == len(pattern):
            indices.append(i - len(pattern) - 1)

    return indices


if __name__ == "__main__":
    string = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"

    print(solve(string, pattern))
