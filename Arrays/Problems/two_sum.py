def solve(arr: list[int], target: int) -> tuple[int, int]:
    m = {}
    for i, n in enumerate(arr):
        if (target - n) in m:
            return m[target - n], i

        m[n] = i

    return -1, -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 13

    print(solve(arr.copy(), target))
