import sys
sys.setrecursionlimit(10**5)
read = sys.stdin.readline

N_marble, N_comp = map(int,read().rstrip().split())

# 작은 녀석들 받기
graph_small = [[] for _ in range(N_marble + 1)]
# 큰 녀석들 받기
graph_big = [[] for _ in range(N_marble + 1)]

visited = [False] * (N_marble+1)

for _ in range(N_comp):
    big, small = map(int,read().rstrip().split())
    graph_small[big].append(small)
    graph_big[small].append(big)

def find_small_dfs(marble):
    global num_small

    visited[marble] = True

    for small in graph_small[marble]:
        # visited False인 곳을 들어갈 수 있나?
        if visited[small] == False:
            find_small_dfs(small)
            # 작은 것 찾아 들어갈 때 마다 small += 1
            num_small += 1

def find_big_dfs(marble):
    global num_big

    visited[marble] = True

    for big in graph_big[marble]:
        # visited True인 곳을 들어갈 수 있나?
        # -- 3은 5보다 크다,  3은 6보다 크다
        # -- 5는 6보다 크다
        if visited[big] == False:
            find_big_dfs(big)
            # 작은 것 찾아 들어갈 때 마다 small += 1
            num_big += 1

mid = (1+N_marble) // 2
ans = 0
for i in range(1,N_marble+1):

    visited = [False] * (N_marble+1)
    num_small = 0
    find_small_dfs(i)
    
    num_big = 0
    find_big_dfs(i)

    if num_small >= mid or num_big >= mid:
        ans += 1

print(ans)