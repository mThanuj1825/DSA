def solve(arr: list[int]) -> int:
    xor = 0
    for n in arr:
        xor ^= n

    return xor


if __name__ == "__main__":
    arr = [1, 5, 6, 1, 4, 6, 5]
    print(solve(arr.copy()))
