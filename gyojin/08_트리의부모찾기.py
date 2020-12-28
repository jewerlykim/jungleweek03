import sys

# sys.stdin = open('input.txt', 'r')
N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    key, value = map(int, sys.stdin.readline().split())
    tree[key].append(value)
    tree[value].append(key)

# visited = [False] * (N+1)
ans = [0] * (N+1)


def parent_dfs(start):
    stack = [start]

    while stack:
        x = stack.pop()

        for node in tree[x]:
            ans[node] = x
            stack.append(node)
            tree[node].remove(x)


parent_dfs(1)
for i in range(2, N+1):
    print(ans[i])
