# 단지 번호 붙이기 bfs
import sys
from collections import deque
# import numpy as np
# sys.stdin = open('/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/practice/2667.txt','r')

city = []
N = int(sys.stdin.readline())
for _ in range(N):
    city.append(list(map(int, sys.stdin.readline().rstrip())))

# city = np.array(city)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 0
append_list = []
def bfs(x,y):
    global count
    append_count = 0
    queue = deque()
    if 0<=x<N and 0<=y<N and city[x][y]==1:
        queue.append((x,y))
        append_count+=1
        city[x][y]=0

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<N and city[nx][ny]==1:
                    city[nx][ny]=0
                    queue.append((nx,ny))
                    append_count+=1
        count += 1
        append_list.append(append_count)

    else:return

for x in range(N):
    for y in range(N):
        bfs(x,y)

print(count)
for i in sorted(append_list):
    print(i)
