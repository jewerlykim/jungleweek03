from collections import deque
import sys
read = sys.stdin.readline


n_point, n_line, strt = map(int,read().rstrip().split())

graph = [[] for _ in range(n_point+1)]

# print(graph)
# 상호 링크 추가 + 정렬해주어야함!!!
for _ in range(n_line):
    point1, point2 = map(int,read().rstrip().split())

    graph[point1].append(point2)
    graph[point2].append(point1)
    graph[point1].sort()
    graph[point2].sort()

# print(graph)
visited_dfs = [False] * (n_point+1)
visited_bfs = [False] * (n_point+1)

def dfs(graph, strt, visited):

    # 나 왔어
    visited[strt] = True
    # print
    print(strt, end = " ")
    
    # 연결된 점 
    for p in graph[strt]:
        if visited[p] == False:
            dfs(graph,p,visited)


def bfs(graph, strt, visited):

    queue = deque([strt])
    # 이미 왔음 처리 필수, 안그러면 다시감
    visited[strt] = True

    while queue:
        now = queue.popleft()
        print(now, end = " ")

        for p in graph[now]:
            if visited[p] == False:
                # 안갔던 점들 모두 queue에 넣는다.
                queue.append(p)
                visited[p] = True


dfs(graph,strt,visited_dfs)
print()
bfs(graph,strt,visited_bfs)
