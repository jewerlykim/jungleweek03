# 미로 탈출 간선의 비용이 모두 같고 최단거리를 구할 때 bfs를 사용
import sys
import numpy as np
from collections import deque

sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/practice/152.txt",'r')

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

graph = np.array(graph)
print(graph)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y =queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx >=N or ny>=M:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[N-1][M-1]

print(bfs(0,0))
print(graph)