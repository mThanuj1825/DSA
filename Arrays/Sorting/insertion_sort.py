def sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        cur = arr[i]
        j = i - 1
        while j > -1 and arr[j] > cur:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = cur

    return arr


if __name__ == "__main__":
    arr = [5, 2, 3, 1, 4]
    print(sort(arr.copy()))
