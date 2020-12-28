import sys
sys.setrecursionlimit(10**5)
read = sys.stdin.readline

n_marble, n_comp = map(int,read().rstrip().split())

# 작은 거 없는 애들 구분
first_small = [True] * (n_marble+1)
first_big =  [True] * (n_marble+1)

# 작은 녀석들 받기
graph_small = [[] for _ in range(n_marble + 1)]
# 큰 녀석들 받기
graph_big = [[] for _ in range(n_marble + 1)]

visited = None

ans_li = [[0,0] for _ in range(n_marble+1)]
# 연결 안된 녀석들, dfs돌릴 녀석들
first = [True] *  (n_marble + 1)

for _ in range(n_comp):

    big, small = map(int,read().rstrip().split())
    
    # 나보다 무거운 녀석들을 담는다.
    graph_big[small].append(big)
    # 얘네는 작은 거 있다.
    first_big[big] = False


    graph_small[big].append(small)
    first_small[small] = False

# 작은 것 개수찾기
def dfs_small(marble,depth):

    visited[marble] = True
    ans_li[marble][0] += depth

    for small in graph_small[marble]:
        if visited[small] == False:
            dfs_small(small,depth + 1)
        elif visited[small] == True:
            ans_li[marble][0] += ans_li[small][0]


# 큰 것 개수찾기
def dfs_big(marble,depth):
    visited[marble] = True
    ans_li[marble][1] += depth
    
    for big in graph_big[marble]:
        if visited[big] == False:
            dfs_big(big, depth + 1)
        # 들어가다가 이미 왔던 놈 만나면,

        elif visited[big] == True:
            ans_li[marble][1] += ans_li[big][1]


visited = [False] * (n_marble + 1)
for i in range(1,n_marble+1):

    # 작은 것 없는 녀석들
    if first_big[i]:
        dfs_big(i,0)
    

visited = [False] * (n_marble + 1)
for i in range(1,n_marble+1):

    if first_small[i]:
        dfs_small(i,0)

mid = (1+n_marble) // 2
ans = 0

for small, big in ans_li:
    if small >= mid or big >= mid:
        ans += 1

print(ans_li)
print(ans)