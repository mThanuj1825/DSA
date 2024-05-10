def solve(arr: list[int]) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2

        if 1 <= arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return low


if __name__ == '__main__':
    arr = [1, 1, 1, 0, 0, 0, 0, 0, 0]
    target = 0
    print(solve(arr.copy()))
