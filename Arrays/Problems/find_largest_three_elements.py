from typing import Tuple


def solve(arr: list[int]) -> tuple[float | int, float | int, float | int]:
    max1 = max2 = max3 = float('-inf')
    for n in arr:
        if n > max1:
            max3 = max2
            max2 = max1
            max1 = n
        elif n > max2:
            max3 = max2
            max2 = n
        elif n > max3:
            max3 = n

    return max1, max2, max3


if __name__ == "__main__":
    arr = [2, 4, 6, 1, 2, 8, 9, 0, 4]
    print(solve(arr.copy()))
