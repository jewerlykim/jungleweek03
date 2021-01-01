import sys
# sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
house = []
for _ in range(N):
    house.append(list(map(int, sys.stdin.readline().rstrip())))

visit = [[0] * N for _ in range(N)]


def dfs(x, y):
    global cnt
    visit[x][y] = 1

    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        xx = x + dx
        yy = y + dy

        if 0 <= xx < N and 0 <= yy < N and house[xx][yy] == 1 and visit[xx][yy] == 0:
            dfs(xx, yy)
            cnt += 1


ans = []
for row in range(N):
    for col in range(N):
        if house[row][col] == 1 and visit[row][col] == 0:
            cnt = 1
            dfs(row, col)
            ans.append(cnt)

ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
