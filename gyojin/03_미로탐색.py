import sys

N, M = map(int, sys.stdin.readline().split())
li = []
for _ in range(N):
    li.append(list(map(int, sys.stdin.readline().rstrip())))


def bfs(graph, x, y):
    visited = [[0] * M for _ in range(N)]
    que = [[x, y]]
    visited[x][y] = 1

    while que:
        top = que.pop(0)
        x, y = top[0], top[1]

        if x == N-1 and y == M-1:
            return visited[N-1][M-1]

        if x - 1 >= 0 and visited[x - 1][y] == 0 and graph[x - 1][y] == 1:
            visited[x - 1][y] += visited[x][y] + 1
            que.append([x - 1, y])
        if x + 1 < N and visited[x + 1][y] == 0 and graph[x + 1][y] == 1:
            visited[x + 1][y] += visited[x][y] + 1
            que.append([x + 1, y])
        if y - 1 >= 0 and visited[x][y - 1] == 0 and graph[x][y - 1] == 1:
            visited[x][y - 1] += visited[x][y] + 1
            que.append([x, y - 1])
        if y + 1 < M and visited[x][y + 1] == 0 and graph[x][y + 1] == 1:
            visited[x][y + 1] += visited[x][y] + 1
            que.append([x, y + 1])


print(bfs(li, 0, 0))
