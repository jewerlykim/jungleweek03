# 구슬 찾기
import sys
# sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/10.txt",'r')

N, M = map(int, sys.stdin.readline().split())
heavy_list = [[] for _ in range(N+1)]
light_list = [[] for _ in range(N+1)]

whole_count = 0 # 전체에서 몇 개가 나오는지 

def dfs(graph, v, visited):
    global count
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
            count += 1



for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    heavy_list[y].append(x)
    light_list[x].append(y)

# print(heavy_list)
# print(light_list)

for i in range(1,N+1):
    count = 0
    heavy_visited = [False]*(N+1)
    light_visited = [False]*(N+1)
    dfs(heavy_list,i,heavy_visited)
    if count>(N//2):
        whole_count += 1
    count=0
    dfs(light_list,i,light_visited)
    if count>(N//2):
        whole_count += 1

print(whole_count)
    
