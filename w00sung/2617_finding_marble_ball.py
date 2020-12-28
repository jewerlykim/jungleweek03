import sys
sys.setrecursionlimit(10**5)
read = sys.stdin.readline

n_marble, n_comp = map(int,read().rstrip().split())
graph = [[] for _ in range(n_marble + 1)]
visited = [False] * (n_marble + 1)
ans_li = [[0,0] for _ in range(n_marble+1)]
# 연결 안된 녀석들, dfs돌릴 녀석들
first = [True] *  (n_marble + 1)
# small_cnt = [0] * (n_marble + 1)
# big_cnt = [0] * (n_marble + 1)
# ans = []

for _ in range(n_comp):

    big, small = map(int,read().rstrip().split())
    
    # 나보다 무거운 녀석들을 담는다.
    graph[small].append(big)
    # 가장 작은 녀석들만 dfs 돌릴거임
    first[big] = False

# 얼마나 더 들어갈 수 있는지 or 얼마나 더 들어왔는지

# marble : 구슬, depth : 깊이 (1부터 시작), n : 구슬 개수
cnt = 0
def count_ball_dfs(marble, depth,mid):
    cnt = 0
    # 가벼운 녀석들 개수
    # small_cnt[marble] += (depth-1)
    
    # 들어왔는데 true?
    if visited[marble] == True:
        ans_li[marble]

    # 가벼운 녀석 개수
    ans_li[marble][1] += (depth-1)

    for bigger in graph[marble]:
        # 찔린 것도 찔릴 수 있게, 들어갈 때 visited 조건 빼준다.
        # if visited[bigger] == False:

        # 들어간 깊이를 받아와서 계속 쌓아줌
        num = count_ball_dfs(bigger,depth + 1,mid)
        
        # 나보다 큰 녀석의 무거운 개수 얹기
        cnt += num 
        # DFS 들어가서 나올 때, + 1
        cnt += 1 

    # 나보다 큰 녀석들 개수 -- depth 들어간 개수
    # big_cnt[marble] = cnt
    # 무거운 녀석이 중앙값 개수보다 크면 출력
    # if cnt >= mid:
    #     ans_li.append(marble)
    
    # 무거운 녀석 수
    ans_li[marble][0] = cnt

    return cnt

mid =(1+n_marble) // 2

# 반드시 1부터 시작하라는 법 없음..
for i in range(1,(n_marble+1)):
    # 얘네 보다 작은 것 없는 녀석들만 dfs돌린다.
    if first[i] == True:
        count_ball_dfs(i,1,mid)

ans = 0
for small, big in ans_li:
    if small >= mid or big >= mid:
        ans += 1

# for i in range(1,n_marble+1):
#     if (small_cnt[i] >= (1+n_marble)//2) or (big_cnt[i] >= (1+n_marble)//2):
#         ans += 1

print(ans)
# print(small_cnt)
# print(big_cnt)