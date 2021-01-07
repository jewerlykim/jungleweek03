import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
check = [False] * (N+1)
indegree = [0] * (N+1)
for _ in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    tree[x].append((y, z))
    indegree[y] += 1
    check[x] = True

que = deque([(N, 1)])
result = [0] * (N+1)

while que:
    node, cnt = que.popleft()

    for (i, j) in tree[node]:
        indegree[i] -= 1
        result[i] += cnt * j
        if indegree[i] == 0:
            que.append((i, result[i]))

for i in range(1, N+1):
    if check[i] is False:
        print(f'{i} {result[i]}')