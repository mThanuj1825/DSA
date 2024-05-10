def solve(arr: list[int], k: int, x: int) -> list[int]:
    res = []

    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2

        if x <= arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    if arr[low] == x:
        left = low - 1
        right = low + 1
    else:
        left = low
        right = low + 1

    for _ in range(k // 2):
        if left > -1:
            res.append(arr[left])
            left -= 1

    for _ in range(k - len(res)):
        if right < len(arr):
            res.append(arr[right])
            right += 1

    return res


if __name__ == '__main__':
    arr = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
    k = 4
    x = 50

    print(solve(arr.copy(), k, x))
