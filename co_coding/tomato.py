import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
li = [[] for _ in range(H)]
tmp = []
for i in range(H):
    for _ in range(N):
        li[i].append(list(map(int, sys.stdin.readline().split())))

que = deque()
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
for i in range(H):
    for j in range(N):
        for k in range(M):
            if li[i][j][k] == 1:
                que.append([i, j, k])
                visited[i][j][k] = 1
            if li[i][j][k] == -1:
                visited[i][j][k] = -1


while que:
    x, y, z = que.popleft()

    if x - 1 >= 0 and visited[x - 1][y][z] == 0 and li[x - 1][y][z] == 0:
        visited[x - 1][y][z] += visited[x][y][z] + 1
        que.append([x - 1, y, z])
    if x + 1 < H and visited[x + 1][y][z] == 0 and li[x + 1][y][z] == 0:
        visited[x + 1][y][z] += visited[x][y][z] + 1
        que.append([x + 1, y, z])
    if z - 1 >= 0 and visited[x][y][z-1] == 0 and li[x][y][z-1] == 0:
        visited[x][y][z-1] += visited[x][y][z] + 1
        que.append([x, y, z-1])
    if z + 1 < M and visited[x][y][z+1] == 0 and li[x][y][z+1] == 0:
        visited[x][y][z+1] += visited[x][y][z] + 1
        que.append([x, y, z+1])
    if y - 1 >= 0 and visited[x][y - 1][z] == 0 and li[x][y - 1][z] == 0:
        visited[x][y - 1][z] += visited[x][y][z] + 1
        que.append([x, y - 1, z])
    if y + 1 < N and visited[x][y + 1][z] == 0 and li[x][y + 1][z] == 0:
        visited[x][y + 1][z] += visited[x][y][z] + 1
        que.append([x, y + 1, z])

maxi = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if visited[i][j][k] == 0:
                print(-1)
                sys.exit()
            maxi = max(maxi, visited[i][j][k])

print(maxi - 1)