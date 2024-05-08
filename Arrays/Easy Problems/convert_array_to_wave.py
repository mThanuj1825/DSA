def solve(arr: list[int]) -> list[int]:
    arr.sort()
    for i in range(0, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


if __name__ == "__main__":
    arr = [6, 7, 3, 5, 1, 10, 9, 2, 4]
    print(solve(arr.copy()))
