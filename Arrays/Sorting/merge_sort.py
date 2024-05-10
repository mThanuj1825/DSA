def sort(arr: list[int]) -> list[int]:
    def merge(left: int, mid: int, right: int) -> None:
        left_size = mid - left + 1
        right_size = right - mid

        left_arr = []
        right_arr = []

        for i in range(left_size):
            left_arr.append(arr[left + i])
        for i in range(right_size):
            right_arr.append(arr[mid + i + 1])

        l, r = 0, 0
        idx = left
        while l < left_size and r < right_size:
            if left_arr[l] < right_arr[r]:
                arr[idx] = left_arr[l]
                l += 1
            else:
                arr[idx] = right_arr[r]
                r += 1
            idx += 1

        while l < left_size:
            arr[idx] = left_arr[l]
            l += 1

        while r < right_size:
            arr[idx] = right_arr[r]
            r += 1

    def perform_sort(left: int, right: int) -> None:
        from Arrays.Sorting import insertion_sort
        if left < right:
            if right - left + 1 < 32:
                insertion_sort.sort(arr)
            else:
                mid = (left + right) // 2

                perform_sort(left, mid)
                perform_sort(mid + 1, right)

                merge(left, mid, right)

    perform_sort(0, len(arr) - 1)
    return arr


if __name__ == "__main__":
    from random import randint
    arr = [randint(0, 10000) for _ in range(1000)]
    print(sort(arr.copy()))
