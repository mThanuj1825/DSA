import random

from methodtime import timeit


@timeit
def search(arr: list[int], target: int) -> int:
    n = len(arr)
    last = arr[n - 1]

    arr[n - 1] = target
    i = 0

    while arr[i] != target:
        i += 1

    arr[n - 1] = last

    if i < n - 1 or arr[n - 1] == target:
        return i

    return -1


if __name__ == "__main__":
    arr = [random.randint(1, 1000) for i in range(100000)]
    target = random.choice(arr)

    print(search(arr, target))
