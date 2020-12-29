# 빙산
import sys
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/9.txt",'r')
import numpy as np
sys.setrecursionlimit(10**9)
N, M = map(int, sys.stdin.readline().split())
graph = []
days = 0

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

graph = np.array(graph)
print(graph)

def dfs(graph, x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    # 현재노드를 아직 방문하지 않았다면
    if graph[x][y] != 0:
        # 해당 노드 방문 처리
            graph[x][y] = 0
            # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
            dfs(graph, x-1, y)
            dfs(graph, x, y-1)
            dfs(graph, x+1, y)
            dfs(graph, x, y+1)
            return True
    return False

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
            if graph[i][j]!=0 and dfs(graph, i, j):
                count += 1
    return count

while True:
    melt_graph = [[0 for _ in range(M)] for _ in range(N)]
    check_graph = [[0 for _ in range(M)] for _ in range(N)]
    check_graph = np.array(check_graph)
    days += 1

    for i in range(N):
        for j in range(M):
            if graph[i][j]!=0:
                graph[i][j] -= melt(graph, i, j)
                if graph[i][j]<0:
                    graph[i][j]=0
                check_graph[i][j] = graph[i][j]
    print(check_graph)

    if check(check_graph)>=2:
        print(days)
        break
    sums = 0
    for i in graph:
        sums+=sum(i)
    if sums==0:
        print(0)
        break
