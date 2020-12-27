# 탈출
import sys
import numpy as np
from collections import deque
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/5.txt", 'r')

R, C = map(int, sys.stdin.readline().split())
forest = []
for _ in range(R):
    forest.append(list(map(str, sys.stdin.readline().rstrip())))

forest = np.array(forest)
print(forest)

water = deque()
hog = deque()

for r in range(R):
    for c in range(C):
        if forest[r][c]=='*':
            water.append((r,c))
        if forest[r][c]=='S':
            hog.append((r,c))
            forest[r][c]=0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs_water():
    while hog:
        x , y = water.popleft()
        p , k = hog.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            np = p + dx[i]
            nk = k + dy[i]
            if 0<=np<R and 0<=nk<C and forest[np][nk]=='D':
                forest[np][nk]=int(forest[p][k])+1
                return forest[np][nk]
            if 0<=nx<R and 0<=ny<C and forest[nx][ny]!='D' and forest[nx][ny]!='X' and forest[nx][ny]!=forest[p][k]:
                forest[nx][ny]='*'
                water.append((nx,ny))
            if 0<=np<R and 0<=nk<C and forest[np][nk]=='.':
                forest[np][nk]=int(forest[p][k])+1
                hog.append((np,nk))
        print(forest)
    return 'KAKTUS'




print(bfs_water())
print(forest)
