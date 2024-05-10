def find_maximum(arr: list[int]) -> int:
    def helper(low: int, high: int) -> int | float:
        if low > high:
            return float('-inf')

        if low == high:
            return arr[low]

        mid = low + (high - low) // 2

        left_max = helper(low, mid)
        right_max = helper(mid + 1, high)

        return max(left_max, right_max)

    return helper(0, len(arr) - 1)


if __name__ == '__main__':
    arr = [0, 2, 4, 6, 1, 2, 19, 8, 20, 93, 45, 64]
    print(find_maximum(arr.copy()))
