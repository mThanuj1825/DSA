def solve(arr: list[int]) -> list[int]:
    arr.sort()
    new_arr = [-1] * len(arr)
    idx = len(arr) - 1

    for i in range(0, len(new_arr), 2):
        new_arr[i] = arr[idx]
        idx -= 1

    for i in range(1, len(new_arr), 2):
        new_arr[i] = arr[idx]
        idx -= 1

    return new_arr


if __name__ == "__main__":
    arr = [1, 3, 2]
    print(solve(arr.copy()))
