# 유기농 배추
import sys
# import numpy as np
from collections import deque
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/practice/1012.txt",'r')

T = int(sys.stdin.readline().strip())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        i, j = map(int, sys.stdin.readline().split())
        graph[j][i]=1
    # graph=np.array(graph)

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    count =0
    def bfs(x,y):
        global count
        queue = deque()
        if graph[x][y]==1:
            queue.append((x,y))
            while queue:
                x,y=queue.popleft()    
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<N and 0<=ny<M and graph[nx][ny]==1:
                        graph[nx][ny]=0
                        queue.append((nx,ny))
            count += 1
    for i in range(N):
        for j in range(M):
            bfs(i,j)

    print(count)
