def sort(arr: list[int]) -> list[int]:
    idx = 0
    while idx < len(arr):
        while arr[idx] != idx + 1:
            cur = arr[idx]
            arr[idx], arr[cur - 1] = arr[cur - 1], arr[idx]
        idx += 1

    return arr


if __name__ == "__main__":
    arr = [6, 7, 3, 5, 1, 10, 9, 2, 4, 8]
    print(sort(arr.copy()))
