def solve(arr: list[int]) -> tuple[int, int]:
    s = set()
    rep = float('inf')
    for n in arr:
        if n in s:
            rep = n
            break
        s.add(n)

    idx = 0
    while idx < len(arr):
        while arr[idx] != idx + 1:
            cur = arr[idx]
            if arr[cur - 1] == cur:
                break
            arr[idx], arr[cur - 1] = arr[cur - 1], arr[idx]
        idx += 1

    for i, n in enumerate(arr):
        if n != i + 1:
            return i + 1, rep

    return -1, rep


if __name__ == '__main__':
    arr = [4, 3, 6, 2, 1, 1]
    print(solve(arr.copy()))
