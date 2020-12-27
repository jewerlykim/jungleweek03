# 2차원 토마토
import sys
import numpy as np
from collections import deque
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/practice/7576.txt",'r')

tomato = []
M,N = map(int, sys.stdin.readline().split())
for _ in range(N):
    tomato.append(list(map(int, sys.stdin.readline().split())))

tomato = np.array(tomato)
print(tomato)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and tomato[nx][ny]==0:
                tomato[nx][ny]=tomato[x][y]+1
                queue.append((nx,ny))

for i in range(N):
    for j in range(M):
        if tomato[i][j]==1:
            bfs(i,j)

is_true = False

for i in tomato:
    if 0 in i:
        is_true=True
print(tomato)
if is_true:
    print(-1)
else:
    max_num=0
    for i in tomato:
        max_num=max(max_num, max(i))
    print(max_num-1)