import sys

N, M, V = map(int, sys.stdin.readline().split())
li = [[] for _ in range(N+1)]
for _ in range(M):
    key, value = map(int, sys.stdin.readline().split())
    li[key].append(value)
    li[value].append(key)


def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        top = stack.pop()
        if top not in visited:
            visited.append(top)
            stack += sorted(graph[top], reverse=True)
    return visited


def bfs(graph, start):
    visited = []
    que = [start]

    while que:
        top = que.pop(0)
        if top not in visited:
            visited.append(top)
            que += sorted(graph[top])
    return visited


print(*dfs(li, V))
print(*bfs(li, V))
