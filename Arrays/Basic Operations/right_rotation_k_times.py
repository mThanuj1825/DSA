def rotate(arr: list[int], k: int) -> list[int]:
    from reverse_an_array import reverse, reverse_range
    reverse(arr)
    reverse_range(arr, 0, k - 1)
    reverse_range(arr, k, len(arr) - 1)

    return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 10

    print(rotate(arr.copy(), k % len(arr)))
