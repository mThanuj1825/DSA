import random

from methodtime import timeit

from Searching.Algorithms import binary_search


@timeit
def search(arr: list[int], target: int) -> int:
    if arr[0] == target:
        return 0

    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2

    return binary_search.search(arr, target, i // 2, min(i, len(arr) - 1))


if __name__ == "__main__":
    arr = [random.randint(1, 1000) for i in range(1000000)]
    arr.sort()
    target = random.choice(arr)

    print(search(arr, target))
