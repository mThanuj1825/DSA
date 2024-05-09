def solve(arr: list[int], target: int) -> tuple[int, int]:
    left, right = 0, 1
    cur_sum = arr[0]

    while right <= len(arr):
        while cur_sum > target and left < right:
            cur_sum -= arr[left]
            left += 1

        if cur_sum == target:
            return left, right - 1

        if right < len(arr):
            cur_sum += arr[right]

        right += 1

    return -1, -1


if __name__ == "__main__":
    arr = [1, 4, 20, 3, 10, 5]
    target = 15

    print(solve(arr.copy(), target))
