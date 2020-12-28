# 트리의 부모 찾기
import sys
# sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/8.txt",'r')
sys.setrecursionlimit(10**9)
# dfs 함수
def dfs(graph, v, visited,parent):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            parent[i] = v
            dfs(graph, i, visited, parent)

# 실행
N = int(sys.stdin.readline().rstrip())
graph = [
    [] for _ in range(N+1)
]
parent = [[0] for _ in range(N+1)]

visited = [False] * 100001

for _ in range(N-1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(graph, 1, visited, parent)
# print(graph)
# print(parent)

for i in parent[2:]:
    print(i)

