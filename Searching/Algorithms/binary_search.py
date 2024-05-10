import random

from methodtime import timeit


@timeit
def search(arr: list[int], target: int, low=0, high=-1) -> int:
    high = len(arr) - 1 if high == -1 else high
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid

        if target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


if __name__ == "__main__":
    arr = [random.randint(1, 1000) for i in range(1000000)]
    arr.sort()
    target = random.choice(arr)

    print(search(arr, target))
