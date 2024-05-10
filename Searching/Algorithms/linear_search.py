import random

from methodtime import timeit


@timeit
def search(arr: list[int], target: int) -> int:
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i

    return -1


if __name__ == "__main__":
    arr = [random.randint(1, 1000) for i in range(100000)]
    target = random.choice(arr)

    print(search(arr, target))
