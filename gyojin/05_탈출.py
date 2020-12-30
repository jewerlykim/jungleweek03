import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
R, C = map(int, sys.stdin.readline().split())
forest = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(R)]

water = deque()
hog = deque()

for i in range(R):
    for j in range(C):
        if forest[i][j] == '*':
            water.append((i, j))
        if forest[i][j] == 'S':
            hog.append((i, j))


def water_bfs():

    # 이동 할당량 저장
    len_water = len(water)

    while len_water > 0:
        x, y = water.popleft()
        len_water -= 1

        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            wx = x + dx
            wy = y + dy

            if 0 <= wx < R and 0 <= wy < C and forest[wx][wy] != 'X' and forest[wx][wy] != '*' and forest[wx][wy] != 'D':
                forest[wx][wy] = '*'
                water.append((wx, wy))


def hog_bfs():
    global day

    # 이동 할당량 저장
    len_hog = len(hog)

    while len_hog > 0:
        x, y = hog.popleft()
        len_hog -= 1

        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            hx = x + dx
            hy = y + dy

            if 0 <= hx < R and 0 <= hy < C and forest[hx][hy] != '*' and forest[hx][hy] != 'X' and forest[hx][hy] != 'S':
                if forest[hx][hy] == 'D': return 1
                forest[hx][hy] = 'S'
                hog.append((hx, hy))


day = 0
while len(hog) > 0:
    day += 1
    water_bfs()

    if hog_bfs() == 1:
        print(day)
        exit()

print('KAKTUS')

