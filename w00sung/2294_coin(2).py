from collections import deque
import sys
read = sys.stdin.readline


N, goal = map(int, read().rstrip().split())
coins = []
for _ in range(N):
    coins.append(int(read()))

# 바로 종료조건 추가
if goal in coins:
    print(1)
    exit()

# 중복값 제거
coins = list(set(coins))

# 큰값부터 넣을 수 있도록 정렬
coins.sort(reverse = True)

# 인덱스로 중복값 제거
# visited = [False] * 10001
visited = [False] * (goal+1)

queue = deque(coins)

cnt = 0

suc = False
while queue:
    cnt += 1
    
    # 레벨 별로 진행됨
    for i in range(len(queue)):
        # queue 개수만큼 한바퀴 돈다.
        now = queue.popleft()

        if now == goal:
            # 레벨 별로 진행 
            # --> 먼저 찾은게 최소 값이다.
            print(cnt)
            exit()
        
        # 중복값 제거하면 시간 줄일 수 있음.
        for coin in coins:
            # 여기서 cnt +1 하고 끝내면
            # 이 level에서 성공하는 것 있는 확률 배제하는것임
            # 메모리 초과 줄이는 방법
            if now + coin <= goal and visited[now+coin] == False:
                queue.append(now+coin)
                visited[now+coin] = True


print(-1)
