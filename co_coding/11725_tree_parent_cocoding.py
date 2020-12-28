import sys
sys.setrecursionlimit(10**5)
read= sys.stdin.readline
N = int(read())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(N-1):
    node1, node2 = map(int,read().rstrip().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

ans = [0] * (N+1)

# print(graph)
def dfs_parent(parent):
    stack = [parent]
    while stack:
        # visited[paretn] == False:
        parent = stack.pop()
        for child in graph[parent]:
            graph[child].remove(parent)
            stack.append(child)
            ans[child] = parent
            #dfs_parent(child)
            
dfs_parent(1)
for i in range(2,N+1):
    print(ans[i])