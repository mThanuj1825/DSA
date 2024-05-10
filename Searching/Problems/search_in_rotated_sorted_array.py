def solve(arr: list[int], target: int) -> int:
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] <= arr[high]:
            if arr[mid] <= target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if arr[low] <= target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

    return -1


if __name__ == '__main__':
    arr = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
    target = 9

    print(solve(arr.copy(), target))
