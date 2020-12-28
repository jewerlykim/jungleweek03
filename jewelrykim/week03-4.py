# 토마토
import sys
# import numpy as np
from collections import deque
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/4.txt",'r')

M, N, H = map(int, sys.stdin.readline().split()) # 가로 세로 높이
boxes = []
for _ in range(H):
    box = []
    for _ in range(N):
        box.append(list(map(int, sys.stdin.readline().split())))
    boxes.append(box)
# boxes = np.array(boxes)

dz = [-1,1,0,0,0,0]
dx = [0,0,-1,1,0,0]
dy = [0,0,0,0,-1,1]

queue = deque()
def bfs():

    while queue:
        z,x,y = queue.popleft()

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if nz<0 or nx<0 or ny<0 or nz>=H or nx>=N or ny>=M:
                continue
            if boxes[nz][nx][ny]==1 or boxes[nz][nx][ny]==-1:
                continue
            if boxes[nz][nx][ny]==0:
                boxes[nz][nx][ny]= boxes[z][x][y]+1
                queue.append((nz,nx,ny))
        # print('##################')
        # print(boxes)


for z in range(H):
    for x in range(N):
        for y in range(M):
            if boxes[z][x][y]==1:
                queue.append((z,x,y))
bfs()
zero_true = False
one_true = False

for z in range(H):
    for x in range(N):
        if 0 in boxes[z][x]:
            zero_true=True
        if 1 in boxes[z][x]:
            one_true=True
# print(zero_true, one_true)

if zero_true:
    print(-1)
elif not one_true:
    print(0)
else:
    max_num=-1
    for z in range(H):
        for x in range(N):
            # print(max(boxes[z][x]))
            max_num = max(max_num, max(boxes[z][x]))
    print(max_num-1)

