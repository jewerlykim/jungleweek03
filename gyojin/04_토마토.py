import sys

M, N, H = map(int, sys.stdin.readline().split())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(N*H)]

tomato = 0
for i in range(N * H):
    for j in range(M):
        if li[i][j] != 0:
            tomato += 1
if tomato == M*N*H:
    print(0)
    sys.exit()

ans = 0
def tomato():
    global ans
    visited = [[-1] * M for _ in range(N*H)]
    que = []

    for i in range(N*H):
        for j in range(M):
            if li[i][j] == 1:
                que.append([i, j])
                visited[i][j] += 1

    while que:
        top = que.pop(0)
        x, y = top[0], top[1]

        if x - 1 >= 0 and visited[x - 1][y] == -1 and li[x - 1][y] == 0:
            visited[x - 1][y] = visited[x][y] + 1
            que.append([x - 1, y])
        if x + 1 < N*H and visited[x + 1][y] == -1 and li[x + 1][y] == 0:
            visited[x + 1][y] = visited[x][y] + 1
            que.append([x + 1, y])
        if x + N < N*H and visited[x + N][y] == -1 and li[x + N][y] == 0:
            visited[x + N][y] = visited[x][y] + 1
            que.append([x + N, y])
        if x - N < N*H and visited[x - N][y] == -1 and li[x - N][y] == 0:
            visited[x - N][y] = visited[x][y] + 1
            que.append([x - N, y])
        if y - 1 >= 0 and visited[x][y - 1] == -1 and li[x][y - 1] == 0:
            visited[x][y - 1] = visited[x][y] + 1
            que.append([x, y - 1])
        if y + 1 < M and visited[x][y + 1] == -1 and li[x][y + 1] == 0:
            visited[x][y + 1] = visited[x][y] + 1
            que.append([x, y + 1])

    for i in range(N * H):
        for j in range(M):
            if visited[i][j] == -1:
                return -1
            ans = max(ans, visited[i][j])
    return ans


print(tomato())
