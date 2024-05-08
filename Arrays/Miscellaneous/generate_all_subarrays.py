def generate(arr: list[int]) -> list[list[int]]:
    sub_arrays = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            sub_arrays.append(arr[i:j])

    return sub_arrays


if __name__ == "__main__":
    arr = [1, 2, 3]
    print(generate(arr.copy()))
