# 장난감 조립 망!
import sys
from collections import deque
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/12.txt",'r')

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

is_middle = [False] * (N+1)
is_middle[N] = True
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
recipy = []

for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x].append((y,z)) # 7은 4로 만들수 있다. 5개가 필요하다
    recipy.append((x,y,z)) # 일단 레서피에 넣어보자
    indegree[y] += 1
    if x!=N:
        is_middle[x] = True # x가 완제품이 아니라면 중간부품이다.

base_num = []
for i in range(1,N+1):
    if is_middle[i]==False:
        base_num.append(i)


def topology_sort():
    result = [0]*(N+1)

    queue = deque()

    for i in range(1, N+1):
        if indegree[i]==0:
            queue.append(i)

    while queue:
        now = queue.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            if is_middle[i]==False: # 기본제품이라면
                pass

            if indegree[i] == 0:
                queue.append(i)

topology_sort()