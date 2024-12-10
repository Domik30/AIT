def is_valid_move(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0

def bfs(grid, start, goal):
    queue = [(start, 0)]
    visited = set()
    visited.add(start)

    while queue:
        current, steps = queue.pop(0)

        if current == goal:
            return steps

        x, y = current
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if is_valid_move(nx, ny, grid) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))

    return -1

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (4, 0)
goal = (2, 4)

steps = bfs(grid, start, goal)
if steps != -1:
    print("počet krtoků", steps)
else:
    print("Cesta neexistuje.")