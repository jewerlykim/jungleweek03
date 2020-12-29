import sys
sys.setrecursionlimit(10**5)
# sys.stdin = open('input.txt', 'r')
N, M = map(int, sys.stdin.readline().split())
ice = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def ice_dfs(x, y):
    global cnt

    visit[x][y] = True

    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        xx = x + dx
        yy = y + dy

        if ice[xx][yy] == 0 and ice[x][y] > 0 and visit[xx][yy] is False:
            ice[x][y] -= 1

        if ice[xx][yy] > 0 and visit[xx][yy] is False:
            cnt += 1
            ice_dfs(xx, yy)


stack = []
for i in range(N):
    for j in range(M):
        if ice[i][j] > 0:
            stack.append((i, j))

year = 0
while True:
    cnt = 1
    visit = [[False] * M for _ in range(N)]
    len_ice = len(stack)
    x, y = stack[-1]

    # 녹이기
    ice_dfs(x, y)
    # print(ice)
    # print(cnt)
    for _ in range(len(stack)):
        i, j = stack.pop(0)
        if ice[i][j] != 0:
            stack.append((i, j))
    # print(stack)

    if not stack:
        print(0)
        exit()

    if cnt < len_ice:
        print(year)
        exit()

    year += 1
    # 녹은 빙산 빼기

