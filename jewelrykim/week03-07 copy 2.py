# 알파벳
import sys
# sys.stdin = open('/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/7.txt', 'r')
R, C = map(int, sys.stdin.readline().split())

visited = [0] * 26
alpha = [list(map(lambda x: ord(x)-65, sys.stdin.readline().strip())) for _ in range(R)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(x,y,z):
    global answer
    answer = max(answer,z)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<R and 0<=ny<C and visited[alpha[nx][ny]]==0:
            visited[alpha[nx][ny]]=1
            dfs(nx, ny, z+1)
            visited[alpha[nx][ny]]=0
            # 다시 돌아가고 싶을때 쓰는 방법 -> 모든 경로 파악//


answer = 1
visited[alpha[0][0]]=1
dfs(0,0, answer)

print(answer)

