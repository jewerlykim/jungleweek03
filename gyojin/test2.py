import sys
from collections import deque

# sys.stdin = open('input.txt', 'r')

N, K = map(int, sys.stdin.readline().split())
if N == K:
    print(0)
    exit()

visit = [False] * 100001

que = deque([N])
visit[N] = True
time = 0
len_que = len(que)

while len_que > 0:

    now = que.popleft()
    len_que -= 1

    for next in (now - 1, now + 1, now * 2):

        if next == K:
            time += 1
            print(time)
            exit()

        if 0 <= next <= 100000 and visit[next] is False:
            visit[next] = True
            que.append(next)

    if len_que == 0:
        time += 1
        len_que = len(que)
