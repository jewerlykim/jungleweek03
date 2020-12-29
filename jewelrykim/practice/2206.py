# 벽 부수고 이동하기
import sys
from collections import deque
# import numpy as np
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/practice/2206.txt",'r')

N, M = map(int, sys.stdin.readline().split())
graph = []


for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))


one_list = []
for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            one_list.append((i,j))

# print(one_list)
# graph = np.array(graph)
# print(graph)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(check_graph):
    queue = deque()
    queue.append((0,0))
    visited[0][0] = False
    graph[0][0]=1
    while queue:
        x,y=queue.popleft()
        if x-1>=0 and graph[x-1][y]==0 and visited[x-1][y]:
            check_graph[x-1][y]=check_graph[x][y]+1
            queue.append((x-1,y))
            visited[x-1][y]=False
        if y-1>=0 and graph[x][y-1]==0 and visited[x][y-1]:
            check_graph[x][y-1]=check_graph[x][y]+1
            queue.append((x,y-1))
            visited[x][y-1]=False
        if x+1<N and graph[x+1][y]==0 and visited[x+1][y]:
            check_graph[x+1][y]=check_graph[x][y]+1
            queue.append((x+1,y))
            visited[x+1][y]=False
        if y+1<M and graph[x][y+1]==0 and visited[x][y+1]:
            check_graph[x][y+1]=check_graph[x][y]+1
            queue.append((x,y+1))
            visited[x][y+1]=False
    graph[0][0]=0
    if check_graph[N-1][M-1]==0:
        return

    return check_graph[N-1][M-1]
check_graph = [[0 for _ in range(M)] for _ in range(N)]
visited = [[True for _ in range(M)] for _ in range(N)]
distance_list = []
x = bfs(check_graph)
if x!=None:
    distance_list.append(x)

for i,j in one_list: # i 를 하나씩 없애가면서 진행해보기
    check_graph = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[True for _ in range(M)] for _ in range(N)]
    check_graph[0][0]=1
    graph[i][j]=0
    x = bfs(check_graph)
    if x!=None:distance_list.append(x)
    graph[i][j]=1
# print(distance_list)
if distance_list:
    print(min(distance_list))
else:print(-1)

