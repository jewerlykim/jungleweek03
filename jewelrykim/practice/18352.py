# 특정 거리의 도시 찾기
import sys
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/practice/18352.txt",'r')
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())

graph = [
    [] for _ in range(N+1)
]
visited = [True] * (N+1)
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)


# print(graph)
ans_list = []
queue = deque()
queue.append((X,0))
def bfs():
    while queue:
        city, cnt = queue.popleft()
        if cnt == K:
            ans_list.append(city)

        visited[city] = False
        for i in graph[city]:
            if visited[i]:
                visited[i]=False
                queue.append((i,cnt+1))

bfs()

if len(ans_list):
    for i in sorted(ans_list):
        print(i)
else:print(-1)
    
