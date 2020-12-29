import sys

sys.stdin = open('../co_coding/input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
ice = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False] * M for _ in range(N)]


def ice_dfs(x, y):
    global cnt
    visited[x][y] = True

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < N and 0 <= y < M:

            if ice[xx][yy] == 0 and ice[x][y] > 0:
                ice[x][y] -= 1

            if ice[xx][yy] > 0 and visited[xx][yy] is False:
                cnt += 1
                ice_dfs(xx, yy)


stack = []

for i in range(N):
    for j in range(M):
        if ice[i][j] > 0:
            stack.append([i, j])

year = 0
while True:
    len_ice = len(stack)
    cnt = 1
    x, y = stack[-1]
    ice_dfs(x, y)
    print(ice)

    for node in stack:
        i, j = node[0], node[1]
        if ice[i][j] <= 0:
            stack.remove(node)

    if cnt < len_ice:
        print(year)
        break
    else:
        year += 1


# year = 0
# while stack:
#     len_ice = len(stack)
#     cnt = 1
#     year += 1
#     x, y = stack[0]
#
#     ice_dfs(x, y)
#     for node in stack:
#         i, j = node[0], node[1]
#         if ice[i][j] == 0:
#             stack.remove(node)
#
#     if cnt < len_ice:
#         print(year)
#         break

# print(0)