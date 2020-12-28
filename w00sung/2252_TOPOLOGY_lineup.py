from collections import deque
import sys
read = sys.stdin.readline

N, M = map(int,read().rstrip().split())
stu = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
queue = deque()
res = [0] * (N+1)

# 삽입 & indegress 정리
for _ in range(M):
    front, back = map(int,read().rstrip().split())
    # 앞 친구의 정보를 넣어준다.
    stu[front].append(back)
    # 나 맞았어
    indegree[back] += 1

# 간선 0 인 녀석들 큐에 삽입
for i in range(1,N+1):
    # indegree 0인 것 삽입
    if indegree[i] == 0:
        queue.append(i)

i = 1
while queue:
    front = queue.popleft()
    res[i] = front
    i += 1
    for back in stu[front]:
        indegree[back] -= 1
        if indegree[back] == 0:
            queue.append(back)


# 간선 0 인 녀석들에 붙어있는 놈들 간선 하나씩 제거
# for i in range(1,N+1):
#     front = queue.popleft()
#     res[i] = front
#     for back in stu[front]:
#         indegree[back] -= 1
#         # 뽑았는데, 0 되면 넣는다.
#         if indegree[back] == 0:
#             queue.append(back)
        
for i in range(1,N+1):
    print(res[i], end= " ")