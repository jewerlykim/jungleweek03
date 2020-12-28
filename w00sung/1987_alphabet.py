import sys
sys.setrecursionlimit(10**5)
read = sys.stdin.readline

# n 행
n, m = map(int, read().rstrip().split())
graph = []

# 상, 하, 좌, 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 2차원 리스트 초기화 후에 & 리스트 넣기
for i in range(n):
    graph.append(list(read().rstrip()))


# 다녀온 알파벳 조회
visited = [False] * 26
max_cnt = -1
# return을 언제 해주는 것이 best 인가?
def dfs(graph,x,y,cnt):
    global max_cnt
    
    cnt += 1
    # 본인 추가
    now = graph[x][y]
    now_idx = ord(now)-65
    visited[now_idx] = True
    
    # 벗어났다.
    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]
    
        # 벽
        if nx < 0 or ny < 0 or nx >= n or ny >= m :
            continue
    
        # 내가 방문했던 녀석이면
        nxt = graph[nx][ny]
        nxt_idx = ord(nxt)-65
        if visited[nxt_idx]:
            continue
        
        # 쭉 들어간다.
        dfs(graph,nx,ny,cnt)

    # 모두 벽이거나, 사방이 막혀있으면, 여기까지온다. 
    # python 시간 절약 -- 만약 여기 까지 오면 끊어주는 return문 작성
    max_cnt = max(max_cnt,cnt)
    visited[now_idx] = False
    cnt -= 1
    return
        
        

dfs(graph,0,0,0)
print(max_cnt)