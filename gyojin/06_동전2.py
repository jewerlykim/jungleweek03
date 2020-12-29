import sys
from collections import deque

# sys.stdin = open('input.txt', 'r')
n, k = map(int, sys.stdin.readline().split())
coins = set(int(sys.stdin.readline()) for _ in range(n))
check = [0] * 100001

que = deque()
for coin in coins:

    if coin == k:
        print(1)
        sys.exit()

    else:
        que.append([coin, 1])
        check[coin] = 1


def coin_bfs():

    while que:
        value, cnt = que.popleft()
        cnt += 1

        for coin in coins:
            if value + coin == k:
                return cnt

            if value + coin < k and check[value + coin] != 1:
                que.append([value + coin, cnt])
                check[value + coin] = 1

            else:
                continue

    return -1


print(coin_bfs())
