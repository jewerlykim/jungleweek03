from collections import deque
import sys
read = sys.stdin.readline

m, n, h = map(int,read().rstrip().split())
tomato = [[] for _ in range(h)]

nontomato = 0
for j in range(h):
    for i in range(n):
        tomato[j].append(list(map(int,read().rstrip().split())))
        nontomato += tomato[j][i].count(0)


# 상, 하, 좌, 우
dx = [1,-1,0,0]
dy = [0,0,-1,1]

# 위, 아래
dz = [-1,1]


# print(nontomato)
# tomato[0][1][3] -- 0층 1행 3열

# 1찾기
queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                queue.append((i,j,k))

# print(queue)

# h층 x행 y열
# x, y, z --- [z][x][y] --- x 상한 : n , y 상한 : m
def bfs(tomato, x,y,z):
    global nontomato

    if nontomato == 0:
        print(0)
        return

    day = 0
    cnt = 0
    # 토마토를 찾아라!
    len_queue = len(queue)
    while queue:


        z,x,y = queue.popleft()
        # 날짜 세기 장치
        cnt += 1

        # 기존에 개수만큼 빠졌으면,
        

        # 상,하,좌,우 검사
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if tomato[z][nx][ny] == 0:
                queue.append((z,nx,ny))
                tomato[z][nx][ny] = day + 1
                nontomato -= 1

                # 날은 적힌 숫자 - 1
                # day = max(day, tomato[h][nx][ny]-1)


        # 위, 아래 검사
        for i in range(2):
            nz = z + dz[i]

            if nz < 0 or nz >= h:
                continue

            if tomato[nz][x][y] == 0:
                queue.append((nz,x,y))
                tomato[nz][x][y] = day + 1
                nontomato -= 1

                # day = max(day, tomato[nz][x][y]-1)
        
        # 날짜는, 삽입값만큼 빠졌을 때, 추가된다.
        if cnt == len_queue and nontomato != 0:
            day += 1
            len_queue = len(queue)
            cnt = 0

        # 딱 맞춰서 or 도중에 지웠으면, 끝났으면 day += 1 안되었다.
        # if cnt <= len_queue and nontomato == 0:
        if nontomato == 0: 
            day += 1
            print(day)
            return


    # 0이 남아있으면,
    if nontomato != 0:
        print(-1)


        
bfs(tomato,0,0,0)