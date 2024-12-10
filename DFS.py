def is_valid_move(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y <len(grid[0]) and grid [x][y] == 0

def dfs(grid, start, goal):
    stack = [(start, 0)]
    visited = set()

    while stack:
        (x, y), steps = stack.pop()

        if (x, y) == goal:
            return steps

        if (x, y) not in visited:
            visited.add((x, y))

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y +dy

                if is_valid_move(nx, ny, grid) and (nx, ny) not in visited:
                    stack.append(((nx, ny), steps + 1))

    return -1

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (4, 0)
goal = (2,4)

steps = dfs(grid, start, goal)
if steps != -1:
    print("počet krtoků", steps)
else:
    print("Cesta neexistuje")