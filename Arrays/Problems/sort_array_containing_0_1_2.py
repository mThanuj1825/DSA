def solve(arr: list[int]) -> list[int]:
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr


if __name__ == "__main__":
    arr = [2, 0, 0, 1, 1, 0, 1, 2, 0, 0]
    print(solve(arr.copy()))
