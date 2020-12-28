import sys
from collections import deque
# import numpy as np
# sys.stdin = open('/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/3.txt', 'r')

N, M = map(int, sys.stdin.readline().split())

maze = []
for _ in range(N):
    maze.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <0 or ny < 0 or nx >=N or ny >= M:
                continue
            if maze[nx][ny]==0:
                continue
            if maze[nx][ny]==1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))
    return maze[N-1][M-1]

print(bfs(0,0))
# maze = np.array(maze)
# print(maze)