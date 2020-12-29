import sys
sys.setrecursionlimit(10**5)
sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
beads = []
check = [[0,0] for _ in range(N+1)]

for _ in range(M):
    h, l = map(int, sys.stdin.readline().split())
    beads.append((h, l))
    # check[l][0] += 1
    # check[h][1] += 1

visit = [False] * M


def dfs_bead(k):

    # 자신보다 가벼운 구슬 개수, 무거운 구슬 개수 저장
    heavy, light = beads[k]

    check[light][0] += 1
    check[heavy][1] += 1

    for i in range(M):

        # 가벼운 구슬은 자기보다 가벼운 구슬이 있는지 탐색
        if beads[i][0] == light and visit[i] is False:

            # 현재의 무거운 구슬보다 가벼운 구슬 수 추가
            check[heavy][1] += 1

            visit[i] = True
            dfs_bead(i)

        # 무거운 구슬은 자기보다 무거운 구슬이 있는지 탐색
        if beads[i][1] == heavy and visit[i] is False:

            # 현재의 가벼운 구슬보다 무거운 구슬 수 추가
            check[light][0] += 1

            visit[i] = True
            dfs_bead(i)


for i in range(M):
    if visit[i] is False:
        dfs_bead(i)

mid = (N+1) // 2
ans = 0
for pair in check:
    if pair[0] >= mid or pair[1] >= mid:
        ans += 1

print(check)
print(ans)
