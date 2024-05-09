import random

from methodtime import timeit


@timeit
def search(arr: list[int], target: int) -> int:
    low, high = 0, len(arr) - 1
    while arr[low] <= target <= arr[high] and low <= high:
        probe = low + (((high - low) * (target - arr[low])) // (arr[high] - arr[low]))

        if arr[probe] == target:
            return probe

        if target < arr[probe]:
            high -= 1
        else:
            low += 1

    return -1


if __name__ == '__main__':
    arr = [random.randint(1, 1000) for i in range(1000000)]
    arr.sort()
    target = random.choice(arr)

    print(search(arr, target))
