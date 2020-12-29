import sys
from collections import deque
sys.setrecursionlimit(10**5)
N, M = map(int, sys.stdin.readline().split())
ice = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def ice_dfs(x, y):
    global cnt

    visit[x][y] = True

    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        xx = x + dx
        yy = y + dy

        # 근처에 바다가 있을 경우 빙산이 녹음
        if ice[xx][yy] == 0 and ice[x][y] > 0 and visit[xx][yy] is False:
            ice[x][y] -= 1

        # 빙산일 경우 이동
        if ice[xx][yy] > 0 and visit[xx][yy] is False:
            cnt += 1
            ice_dfs(xx, yy)


# 현재 빙산을 배열에 저장
que = deque()
for i in range(N):
    for j in range(M):
        if ice[i][j] > 0:
            que.append((i, j))

year = 0
while True:
    cnt = 1

    # 빙산 방문 체크
    visit = [[False] * M for _ in range(N)]

    # 현재 남은 빙산의 수
    len_ice = len(que)
    x, y = que[-1]

    # 빙산 녹이기
    ice_dfs(x, y)

    for _ in range(len(que)):

        # 빙산이 녹았을 경우 배열에서 삭제
        # 만약 빙산이 다 녹지 않았으면 다시 추가
        i, j = que.popleft()
        if ice[i][j] != 0:
            que.append((i, j))

    # 빙산이 모두 녹아 2덩어리로 분류되지 못할 때
    if not que:
        print(0)
        exit()

    # 재귀함수 호출 횟수와 빙산 수가 같지 않을 때
    # 즉, 2덩어리로 나뉘어져 DFS가 중도에 멈추게 될 때
    if cnt < len_ice:
        print(year)
        exit()

    # 다음 년도로
    year += 1
