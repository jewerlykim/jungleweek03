# 동전 2 
import sys
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/6.txt",'r')
from collections import deque

# 정보 받기
n, k = map(int, sys.stdin.readline().split())
coins = {int(sys.stdin.readline()) for _ in range(n)}

queue = deque()

check = [9999999999] * (k+1)

def bfs():
    while queue:
        t, cnt = queue.popleft() # 큐에있는 동전과 카운트
        cnt += 1
        for coin in coins:
            nt = t + coin # 큐에서 나온 동전에 다른 동전 추가한 값
            if nt < k: # 그 값이 원하는 값보다 작다면
                if check[nt] > cnt:
                    queue.append([nt, cnt])
                    check[nt] = cnt
            elif nt ==k:
                return cnt
    return -1

for coin in coins: # 원하는 값보다 큰 코인은 배제하고 작은 코인은 큐에 저장
    if coin<=k:
        queue.append([coin,1])
        check[coin] = 1 # 코인의 사용 개수 기본 1

if check[k]==1: # 하나의 코인으로 원하는 값에 도달했을 때 
    print(1)
else:
    print(bfs()) # 그게 아니라면 함수 실행


# print(coins)