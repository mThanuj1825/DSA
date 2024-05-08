def sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


if __name__ == "__main__":
    arr = [5, 2, 3, 1, 4]
    print(sort(arr.copy()))
