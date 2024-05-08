def solve(arr: list[int]) -> list[int]:
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return arr


if __name__ == "__main__":
    arr = [2, 3, 0, 6, 0, 1, 2, 0, 7, 0, 0, 5, 6]
    print(solve(arr.copy()))
