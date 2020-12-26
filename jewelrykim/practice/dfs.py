def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2,3],
    [1,5],
    [1,4],
    [3,5],
    [2,4]
]

visited = [False] * 1001

dfs(graph, 1000, visited)