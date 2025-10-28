def diamond(n):
    # n is number of rows in the upper half (excluding center if n counts upper)
    # total height = 2*n - 1
    for i in range(1, n+1):
        print(' ' * (n - i) + '* ' * i)
    for i in range(n-1, 0, -1):
        print(' ' * (n - i) + '* ' * i)

if __name__ == "__main__":
    diamond(5)
