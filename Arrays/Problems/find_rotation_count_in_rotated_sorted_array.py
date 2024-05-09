def solve(arr: list[int]) -> int:
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return i

    return 0


if __name__ == "__main__":
    arr = [7, 9, 11, 12, 5]
    print(solve(arr.copy()))
