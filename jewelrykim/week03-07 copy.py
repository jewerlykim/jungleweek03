# 알파벳
import sys
# sys.stdin = open('/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/7.txt', 'r')


R, C = map(int, sys.stdin.readline().split())
alpha = []
visited = [False] * 27
for _ in range(R):
    alpha.append(list(map(str, sys.stdin.readline().rstrip())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(x,y,z):
    global answer
    answer = max(answer,z)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<R and 0<=ny<C and not visited[ord(alpha[nx][ny])-64]:
            visited[ord(alpha[nx][ny])-64]=True
            dfs(nx, ny, z+1)
            visited[ord(alpha[nx][ny])-64]=False
            # 다시 돌아가고 싶을때 쓰는 방법 -> 모든 경로 파악//


answer = 1
visited[ord(alpha[0][0])-64]=True
dfs(0,0, answer)

print(answer)

