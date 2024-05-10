from Arrays.Sorting.merge_sort import sort


def solve(arr: list[int]) -> list[tuple[int, int, int]]:
    res = []

    arr = sort(arr)
    for i in range(len(arr) - 2):
        left, right = i + 1, len(arr) - 1
        target = -arr[i]

        while left < right:
            cur_sum = arr[left] + arr[right]

            if cur_sum == target:
                res.append((arr[i], arr[left], arr[right]))
                break

            if cur_sum < target:
                left += 1
            else:
                right -= 1

    return res


if __name__ == '__main__':
    arr = [0, -1, 2, -3, 1]
    print(solve(arr.copy()))
