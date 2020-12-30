import sys

sys.setrecursionlimit(10 ** 5)
# sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
lighter = [[] for _ in range(N + 1)]
heavier = [[] for _ in range(N + 1)]

for _ in range(M):
    h, l = map(int, sys.stdin.readline().split())
    lighter[l].append(h)
    heavier[h].append(l)


def dfs_light(x):
    cnt = 1
    # 자신보다 가벼운 구슬 개수, 무거운 구슬 개수 저장
    l_visit[x] = True

    for node in lighter[x]:

        # 가벼운 구슬은 자기보다 가벼운 구슬이 있는지 탐색
        if l_visit[node] is False:
            # 그 구슬보다 더 가벼운 구슬 dfs 탐색
            cnt += dfs_light(node)

    return cnt


def dfs_heavy(x):
    cnt = 1
    h_visit[x] = True

    for node in heavier[x]:

        # 무거운 구슬은 자기보다 무거운 구슬이 있는지 탐색
        if h_visit[node] is False:
            # 그 구슬보다 더 무거운 구슬 dfs 탐색
            cnt += dfs_heavy(node)

    return cnt


mid = (N + 1) // 2
ans = 0

for i in range(1, N + 1):

    # 방문배열 초기화
    l_visit = [False] * (N + 1)
    h_visit = [False] * (N + 1)

    # 자신보다 무겁거나 가벼운 구슬 수가 중간지점보다 클 때
    if dfs_light(i) > mid or dfs_heavy(i) > mid:
        ans += 1


print(ans)
