def solve(arr: list[int]) -> list[int]:
    idx = 0
    while idx < len(arr):
        while arr[idx] >= 0 and arr[idx] != idx:
            cur = arr[idx]
            arr[idx], arr[cur] = arr[cur], arr[idx]

        idx += 1

    return arr


if __name__ == "__main__":
    arr = [7, 0, 3, 6, 1, 8, 9, 5, 2, 4]
    print(solve(arr.copy()))
