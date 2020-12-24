from collections import deque
import sys
read = sys.stdin.readline

maze = []
n, m = map(int, read().rstrip().split())

# 미로 확인
# 붙어서 받을 때는, split 안하게 주의하자
for _ in range(n):
    maze.append(list(map(int,read().rstrip())))

# # visited : n x m 방문 행렬 -- 사용하지 않음
# visited = [[False] * n for _ in range(m)]

# 상, 하, 좌, 우 움직임
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 상, 하, 좌, 우 모두 연결 필요!
def bfs(maze,n,m):

    
    # 첫 값 1임을 이용
    # 덱에서 좌표 꺼내 쓸 것이다.
    queue = deque()
    queue.append((0,0))

    ## queue = deque([0,0])


    while queue:

        x,y = queue.popleft()

        # 받는 점마다 상,하,좌,우 bfs 시작
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어남 (n,m 이 경계) or 초기값
            if (nx == 0 and ny ==0) or (nx < 0 or nx >= n or ny < 0 or ny >= m):
                continue
            
            # 움직일 수 없음
            if maze[nx][ny] == 0 :
                continue
            
            # 갈 수 있고, 한번도 오지 않은 길이면 + 1
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                
                # queue에 넣어줌
                queue.append((nx,ny))

    print(maze[n-1][m-1])

bfs(maze,n,m)