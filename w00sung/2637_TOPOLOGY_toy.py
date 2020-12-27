from collections import deque
import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

N = int(read())
M = int(read())

# 큐를 활용한 위상정렬
queue = deque()
indegree = [0] * (N+1)
graph = [ [] for _ in range(N+1) ]

# 기본이냐 아니냐
basic = [True] * (N+1)
res = [0] * (N+1)

for _ in range(M):

    main, sub, sub_piece = map(int,read().rstrip().split())
    
    # main이 sub를 향하고있다.
    graph[main].append((sub,sub_piece))
    # 화살표 향하고 있는 간선 + 1
    # 기본제품 X
    basic[main] = False
    indegree[sub] += 1

queue.append((N,1))

while queue:
    
    now, piece = queue.popleft()
    # 필요한 것, 필요한 개수
    
    # 기본 제품이면,
    if basic[now]:
        res[now] = piece

    for sub, sub_piece in graph[now]:
        # 연결선 제거
        indegree[sub] -= 1
        # 연결선 더이상 없으면
        res[sub] += sub_piece * piece

        if indegree[sub] == 0:
            #큐에 넣는다.
            queue.append((sub, res[sub]))  

for i in range(1,N+1):
    if basic[i]:
        print(i,res[i])