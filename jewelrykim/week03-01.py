import sys
from collections import deque
#sys.stdin = open('/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/1.txt','r')

N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
d_visited = [False] * 1001
b_visited = [False] * 1001
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()

#print(graph)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        visited[v] = True
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(graph,V,d_visited)
print()
bfs(graph, V, b_visited)
