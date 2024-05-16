from Queues.Implementations.queue import Queue


def solve(grid: list[list[int]]) -> int:
    def bfs(i, j) -> int:
        transform_x = [1, 0, -1, 0]
        transform_y = [0, 1, 0, -1]

        q = Queue()
        visited = set()

        q.enqueue((i, j, 0))

        max_level = 0

        while not q.is_empty():
            cur = q.dequeue()
            max_level = max(max_level, cur[2])

            visited.add(cur[:-1])

            for _x, _y in zip(transform_x, transform_y):
                new = (cur[0] + _x, cur[1] + _y, cur[2] + 1)
                if new[0] < 0 or new[1] < 0 or new[0] >= len(grid) or new[1] >= len(grid[i]) or new[:-1] in visited:
                    continue

                q.enqueue(new)

        return max_level

    m = float('inf')
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                m = min(m, bfs(i, j))

    return m


if __name__ == '__main__':
    grid = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]

    print(solve(grid))
