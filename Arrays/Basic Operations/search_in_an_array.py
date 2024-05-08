def search(arr: list[int], key: int) -> int:
    for i in range(len(arr)):
        if arr[i] == key:
            return i

    return -1


def get_indices(arr: list[int], key: int) -> list[int]:
    indices = []
    for i in range(len(arr)):
        if arr[i] == key:
            indices.append(i)

    return indices


if __name__ == "__main__":
    arr = [2, 5, 2, 1, 2, 0, 9, 7, 6, 7, 8]
    key = 2

    print(search(arr, key))
    print(get_indices(arr, key))
