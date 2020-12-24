import sys

computer = int(sys.stdin.readline())
pair = int(sys.stdin.readline())
li = [[] for _ in range(computer + 1)]

for _ in range(pair):
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


print(len(dfs(li, 1)) - 1)
