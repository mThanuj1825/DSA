def solve(arr: list[int]) -> list[int]:
    j = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(solve(arr.copy()))
