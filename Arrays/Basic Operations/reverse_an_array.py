def reverse(arr: list[int]) -> list[int]:
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


def reverse_range(arr: list[int], left: int, right: int) -> list[int]:
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(reverse(arr.copy()))
    print(reverse_range(arr.copy(), 0, 2))