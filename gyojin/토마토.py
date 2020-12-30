import sys
from collections import deque

# sys.stdin = open('input.txt', 'r')
M, N, H = map(int, sys.stdin.readline().split())
tomato = [[] for _ in range(H)]
nontomato = 0

for i in range(H):
    for j in range(N):
        tomato[i].append(list(map(int, sys.stdin.readline().split())))
        # 안익은 토마토 개수 세기
        nontomato += tomato[i][j].count(0)

que = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):

            # 익은 토마토 큐에 넣기
            if tomato[i][j][k] == 1:
                que.append([i, j, k])


def tomato_bfs():
    global nontomato

    # 모두 익어있으면 0 출력
    if non_tomato == 0:
        print(0)
        sys.exit()

    day = 0
    cnt = 0

    len_que = len(que)

    while que:
        x, y, z = que.popleft()
        cnt += 1

        # 상, 하, 좌, 우, 윗칸, 아래칸 탐색
        for dx, dy, dz in (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1):
            xx = x + dx
            yy = y + dy
            zz = z + dz

            if 0 <= xx < H and 0 <= yy < N and 0 <= zz < M and tomato[xx][yy][zz] == 0:
                que.append([xx, yy, zz])
                tomato[xx][yy][zz] = 1
                non_tomato -= 1

        # 모든 토마토가 익으면 날짜 출력
        if non_tomato == 0:
            day += 1
            print(day)
            exit()

        # 주변을 탐색해야 하는 토마토 모두 탐색하면
        if cnt == len_que and non_tomato > 0:
            # 할당량 초기화 (주변을 탐색해야 하는 토마토 개수)
            len_que = len(que)
            day += 1
            cnt = 0

    # 토마토가 모두 익지 못하면 -1 출력
    if non_tomato > 0:
        print(-1)


tomato_bfs()
