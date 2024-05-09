import random

from methodtime import timeit


@timeit
def search(arr: list[int], target: int) -> int:
    fib_m_m_2 = 0
    fib_m_m_1 = 1
    fib_m = fib_m_m_2 + fib_m_m_1
    n = len(arr)

    while fib_m < n:
        fib_m_m_2 = fib_m_m_1
        fib_m_m_1 = fib_m
        fib_m = fib_m_m_2 + fib_m_m_1

    offset = -1

    while fib_m > 1:
        i = min(offset + fib_m_m_2, n - 1)

        if arr[i] == target:
            return i

        if target > arr[i]:
            fib_m = fib_m_m_1
            fib_m_m_1 = fib_m_m_2
            fib_m_m_2 = fib_m - fib_m_m_1

            offset = i
        else:
            fib_m = fib_m_m_2
            fib_m_m_1 = fib_m_m_1 - fib_m_m_2
            fib_m_m_2 = fib_m - fib_m_m_1

    if fib_m_m_1 and arr[n - 1] == target:
        return n - 1

    return -1


if __name__ == "__main__":
    arr = [random.randint(1, 1000) for i in range(1000000)]
    arr.sort()
    target = random.choice(arr)

    print(search(arr, target))
