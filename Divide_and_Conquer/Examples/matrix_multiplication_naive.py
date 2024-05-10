import random


# @timeit
def multiply(matrix_a: list[list[int]], matrix_b: list[list[int]], rows: int, cols: int) -> list[list[int]]:
    matrix_res = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            for k in range(rows):
                matrix_res[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return matrix_res


if __name__ == '__main__':
    rows = cols = 10
    min_val = 0
    max_val = 9
    matrix_a = [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]
    matrix_b = [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

    print(matrix_a)
    print(matrix_b)

    print(multiply(matrix_a, matrix_b, rows, cols))
