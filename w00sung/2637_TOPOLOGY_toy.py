from collections import deque
import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

N = int(read())
M = int(read())

indegree = [] * (N+1)
graph = [ [] for _ in range(N+1) ]

for _ in range(M):

    main, sub, sub_piece = map(int,read().rstrip().split())
    # 향하는 행렬 정리

    # main이 sub를 향하고있다.
    graph[main].append(sub)
    indegree[sub] += sub_piece

def topology_toy():
    result = []
    q = deque()

    for i in range(1,N+1):
        # 간선 0 인 것 큐에 넣는다.
        if indegree[i] == 0:
            q.append(i)

    # 기본 부품들의 진입 차수 !!
    while q:
        now = q.popleft()

