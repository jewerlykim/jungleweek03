from collections import deque
import sys
read= sys.stdin.readline

n_comp= int(read())
n_line = int(read())
graph = [[] for _ in range(n_comp+1)]


# 연결 설정
for _ in range(n_line):
    comp1, comp2 = map(int,read().rstrip().split())
    graph[comp1].append(comp2)
    graph[comp2].append(comp1)
    
visited = [False] * (n_comp+1)


def bfs(graph,strt,visited,cnt):

    visited[strt] = True

    queue = deque([strt])

    while queue:

        now = queue.popleft()
        for i in graph[now]:
            if visited[i] == False:

                queue.append(i)
                visited[i] = True
                cnt += 1

    return cnt

print(bfs(graph,1,visited,0))