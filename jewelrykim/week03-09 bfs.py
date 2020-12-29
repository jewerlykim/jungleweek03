# 빙산
import sys
from collections import deque
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/9.txt",'r')
# import numpy as np
sys.setrecursionlimit(10**9)
N, M = map(int, sys.stdin.readline().split())
graph = []
days = 0

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

# graph = np.array(graph)
# print(graph)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(graph, x, y):

    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()

        if x-1>=0 and graph[x-1][y] != 0:
            queue.append((x-1,y))
            graph[x-1][y] = 0
        if x+1<=N and graph[x+1][y] != 0:
            queue.append((x+1,y))
            graph[x+1][y] = 0
        if y-1>=0 and graph[x][y-1] != 0:
            queue.append((x,y-1))
            graph[x][y-1] = 0
        if y+1<=M and graph[x][y+1] != 0:
            queue.append((x,y+1))
            graph[x][y+1]=0



def melt(graph, x, y):
    count = 0
    if 1<=x:
        if graph[x-1][y]==0:
            count += 1
    if x<=N-2:
        if graph[x+1][y]==0:
            count += 1
    if 1<=y:
        if graph[x][y-1]==0:
            count += 1
    if y<=M-2:
        if graph[x][y+1]==0:
            count += 1
    return count


def check(graph):
    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j]!=0:
                bfs(graph, i, j)
                count += 1
    return count

while True:
    melt_graph = [[0 for _ in range(M)] for _ in range(N)]
    check_graph = [[0 for _ in range(M)] for _ in range(N)]
    days += 1

    for i in range(N):
        for j in range(M):
            if graph[i][j]!=0:
                melt_graph[i][j] = melt(graph, i, j)

    for i in range(N):
        for j in range(M):
            if graph[i][j]!=0:
                graph[i][j] -= melt_graph[i][j]
                if graph[i][j]<0:
                    graph[i][j]=0
                check_graph[i][j] = graph[i][j]

    if check(check_graph)>=2:
        print(days)
        break
    sums = 0
    for i in graph:
        sums+=sum(i)
    if sums==0:
        print(0)
        break



