import sys

R, C = map(int, sys.stdin.readline().split())
li = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(R)]
print(li)

def escape():
    sink = [[0] * C for _ in range(R)]

    hedgehog = []
    water = []
    beaver = []

    for i in range(R):
        for j in range(C):
            if li[i][j] == 'S':
                hedgehog.append([i, j])
            elif li[i][j] == '*':
                water.append([i, j])
            elif li[i][j] == 'D':
                beaver.append(i)
                beaver.append(j)

    # movement
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while water:
        top = water.pop(0)
        x, y = top[0], top[1]

        for i in range(4):
            wx = x + dx[i]
            wy = y + dy[i]

            if 0 <= wx < C and 0 <= wy < R and sink[wx][wy] == 0 and li[wx][wy] == '.':
                sink[wx][wy] += sink[x][y] + 1
                water.append([wx, wy])

    time = 0
    while hedgehog:
        top = hedgehog.pop(0)
        x, y = top[0], top[1]

        if x == beaver[0] and y == beaver[1]:
            return time

        for i in range(4):
            hx = x + dx[i]
            hy = y + dy[i]

            if 0 <= hx < C and 0 <= hy < R and sink[hx][hy] > time and li[hx][hy] == '.':
                hedgehog.append([hx, hy])

    return 'KAKTUS'


print(escape())
