def search(arr: list[int], target: int) -> int:
    for i, n in enumerate(arr):
        if n == target:
            return i

    return -1


if __name__ == "__main__":
    arr = [5, 2, 3, 1, 4]
    target = 3
    print(search(arr.copy(), target))
