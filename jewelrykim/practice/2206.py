# 벽 부수고 이동하기
import sys
from collections import deque
import numpy as np
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/practice/2206.txt",'r')

N, M = map(int, sys.stdin.readline().split())
graph = []
visited = [[True for _ in range(M)] for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

graph = np.array(graph)
print(graph)
cant_go = True
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    global cant_go
    queue = deque()
    queue.append((0,0))
    graph[0][0] = 1

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] and graph[nx][ny]==0:
                graph[nx][ny] = graph[x][y] + 1
                visited[x][y]=False
                queue.append((nx,ny))
                cant_go = False
        if cant_go:
            pass
    
    return graph[N-1][M-1]

print(bfs())
