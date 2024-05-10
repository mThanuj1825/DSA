def solve(arr: list[int]) -> int | float:
    s = {}
    min_idx = len(arr) - 1

    for i, n in enumerate(arr):
        if n in s:
            min_idx = min(min_idx, s[n])
        s[n] = i

    return arr[min_idx]


if __name__ == '__main__':
    arr = [6, 10, 5, 4, 9, 120, 4, 6, 10]

    print(solve(arr.copy()))
