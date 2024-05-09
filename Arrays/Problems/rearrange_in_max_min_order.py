def solve(arr: list[int]) -> list[int]:
    new_arr = [-1] * len(arr)
    mx, mn = len(arr) - 1, 0
    idx = 0

    while mn <= mx:
        new_arr[idx] = arr[mx]
        if idx + 1 < len(new_arr):
            new_arr[idx + 1] = arr[mn]

        mx -= 1
        mn += 1
        idx += 2

    return new_arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(solve(arr.copy()))
