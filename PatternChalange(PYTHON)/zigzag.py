# Parshwa Kansara 

def zigzag(total_cols, rows=3):
    grid = [[' ']*total_cols for _ in range(rows)]
    r = 0
    direction = 1  # 1 down, -1 up
    for c in range(total_cols):
        grid[r][c] = '*'
        r += direction
        if r == rows:    # went past bottom
            r = rows - 2
            direction = -1
        elif r == -1:    # went past top
            r = 1
            direction = 1
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    zigzag(30, rows=4)
