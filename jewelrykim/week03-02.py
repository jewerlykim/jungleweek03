# 바이러스 dfs
import sys
# sys.stdin = open('/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/2.txt','r')

computers = int(sys.stdin.readline())
connects = int(sys.stdin.readline())
graph = [[] for _ in range(computers+1)]
visited = [False] * 101
for _ in range(connects):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()
count = 0
def dfs(graph, v, visited):
    global count
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            count += 1
            dfs(graph, i, visited)


dfs(graph, 1, visited)
print(count)