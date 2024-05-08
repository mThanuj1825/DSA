def solve(arr: list[int]) -> list[int]:
    m = {}
    res = []

    for i in arr:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1

    for k, v in m.items():
        if v == 1:
            res.append(k)

    return res


if __name__ == "__main__":
    arr = [2, 4, 5, 1, 2, 3, 5, 8, 9, 4, 3, 2]
    print(solve(arr.copy()))