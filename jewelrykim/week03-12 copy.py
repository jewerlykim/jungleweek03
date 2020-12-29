# 장난감 조립
import sys
from collections import deque
# import numpy as np
# sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/12.txt",'r')

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

is_middle = [False] * (N+1)
is_middle[0] = True
is_middle[N] = True
indegree = [0] * (N+1)
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
in_graph = [[] for _ in range(N+1)]
# graph = np.array(graph)
# print(graph)

for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x][y] = z # 7은 4로 만들수 있다. 5개가 필요하다
    in_graph[x].append(y)
    indegree[y] += 1
    if x!=N:
        is_middle[x] = True # x가 완제품이 아니라면 중간부품이다.

# print(in_graph)
# print(graph)
# base_num = []
# for i in range(1,N+1):
#     if is_middle[i]==False:
#         base_num.append(i)

# print(indegree)
def topology_sort():
    result = [0]*(N+1)# [00005230]
    result[N]=1

    queue = deque()

    for i in range(1, N+1):
        if indegree[i]==0:
            queue.append(i)

    while queue:
        now = queue.popleft()

        for i in in_graph[now]:
            indegree[i] -= 1

            result[i] += graph[now][i]*result[now]
            if indegree[i] == 0:
                queue.append(i)
    return result

for i,v in enumerate(topology_sort()):
    if is_middle[i]==False:
        print(i,v)
