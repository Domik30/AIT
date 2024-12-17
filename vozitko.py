def bfs(grid, R, C, F, S_row, S_col, T_row, T_col):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = [(S_row, S_col, 0, 0)]
    visited = [[[False for _ in range(F + 1)] for _ in range(C)] for _ in range(R)]
    visited[S_row][S_col][0] = True

    while queue:
        row, col, steps, danger_count = queue.pop(0)

        if row == T_row and col == T_col:
            return steps

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < R and 0 <= new_col < C:
                new_danger_count = danger_count + grid[new_row][new_col]

                if new_danger_count <= F and not visited[new_row][new_col][new_danger_count]:
                    visited[new_row][new_col][new_danger_count] = True
                    queue.append((new_row, new_col, steps + 1, new_danger_count))

    return -1


def main():
    print("Zadejte první řádek (R, C, F):")
    R, C, F = map(int, input().split())
    print("Načteno: R=", R, "C=", C, "F=", F)

    print("Zadejte druhý řádek (S_row, S_col, T_row, T_col):")
    S_row, S_col, T_row, T_col = map(int, input().split())
    print("Načteno: Start=(", S_row, ",", S_col, "), Cíl=(", T_row, ",", T_col, ")")

    S_row -= 1
    S_col -= 1
    T_row -= 1
    T_col -= 1

    grid = []
    print("Zadejte mřížku (R řádků, každá s C čísly):")
    for i in range(R):
        row = list(map(int, input().split()))
        grid.append(row)
    result = bfs(grid, R, C, F, S_row, S_col, T_row, T_col)

    print("Výsledek:")
    print(result)

main()
