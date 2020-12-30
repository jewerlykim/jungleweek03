import sys
from collections import deque

# sys.stdin = open('input.txt', 'r')
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
toy = [[] for _ in range(N + 1)]

# 부품 Y 자리에 부품 X를 만드는 데 K개가 드는 정보 저장
for _ in range(M):
    X, Y, K = map(int, sys.stdin.readline().split())
    toy[Y].append((X, K))


def assembly():
    que = deque()
    in_degree = [0] * (N + 1)
    ans = [[0] * (N + 1) for _ in range(N + 1)]

    # 필요한 부품의 수만큼 진입차수 증가
    for i in range(1, N + 1):
        for part in toy[i]:
            in_degree[part[0]] += 1

    # 진입차수가 0인 기본부품 큐에 넣기
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            que.append(i)
            ans[i][i] = 1

    while que:
        cur = que.popleft()

        for (next, cnt) in toy[cur]:

            # next 부품의 진입차수 차감
            in_degree[next] -= 1

            # next 부품의 필요부품 배열에 cur 부품의 개수 누적
            for i in range(N + 1):
                ans[next][i] += ans[cur][i] * cnt

            # next 부품의 진입차수가 0이 되면 큐에 넣기
            if in_degree[next] == 0:
                que.append(next)

    for i in range(1, N + 1):
        if ans[N][i]:
            print(f'{i} {ans[N][i]}')


assembly()
