import sys

R, C = map(int, sys.stdin.readline().split())
# 아스키코드 변환하기 배웠음 #
li = [list(map(lambda x: ord(x) - 65, sys.stdin.readline().rstrip())) for _ in range(R)]

# 아스키코드를 쓰면 미리 배열을 선언하고 비교할 수 있어 딕셔너리보다 효율적 #
visited = [0] * 26
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def alphabet(x, y, cnt):
    global maxi

    maxi = max(maxi, cnt)

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < R and 0 <= yy < C and visited[li[xx][yy]] == 0:
            visited[li[xx][yy]] = 1
            alphabet(xx, yy, cnt+1)
            visited[li[xx][yy]] = 0

    return maxi


visited[li[0][0]] = 1
maxi = 1
print(alphabet(0, 0, 1))
