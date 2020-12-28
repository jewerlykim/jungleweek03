# 탈출
import sys
import numpy as np
from collections import deque

from numpy.lib.stride_tricks import DummyArray
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/5.txt", 'r')

R, C = map(int, sys.stdin.readline().split())
forest = []
for _ in range(R):
    forest.append(list(map(str, sys.stdin.readline().rstrip())))

# forest = np.array(forest)
print(forest)
water = deque()
hog = deque()

for i in range(R):
    for j in range(C):
        if forest[i][j]=='*':
            water.append((i,j))
        if forest[i][j]=='S':
            hog.append((i,j))

def water_bfs():
    len_water = len(water)
    
    while len_water>0:
        x, y = water.popleft()
        len_water -= 1

        if x-1>=0 and forest[x-1][y]!='X' and forest[x-1][y]!='D':
            forest[x-1][y] = '*'
            water.append((x-1,y))

        if x+1<R and forest[x+1][y]!='X' and forest[x+1][y]!='D':
            forest[x+1][y] = '*'
            water.append((x+1,y))

        if y-1>=0 and forest[x][y-1]!='X' and forest[x][y-1]!='D':
            forest[x][y-1] = '*'
            water.append((x,y-1))

        if y+1<C and forest[x][y+1]!='X' and forest[x][y+1]!='D':
            forest[x][y+1] = '*'
            water.append((x,y+1))
        
    
        

def hog_bfs():
    len_hog = len(hog) # today's 할당량
    # move = 0
    while len_hog>0:
        x, y = hog.popleft()
        len_hog -= 1

        if x-1>=0 and forest[x-1][y]!='X' and forest[x-1][y]!='*':
            if forest[x-1][y]=='D':return 1
            forest[x-1][y] = 'S'
            hog.append((x-1,y))
            # move +=1

        if x+1<R and forest[x+1][y]!='X' and forest[x+1][y]!='*':
            if forest[x+1][y] == 'D': return 1
            forest[x+1][y] = 'S'
            hog.append((x+1,y))
            # move +=1
            

        if y-1>=0 and forest[x][y-1]!='X' and forest[x][y-1]!='*':
            if forest[x][y-1] == 'D': return 1
            forest[x][y-1] = 'S'
            hog.append((x,y-1))
            # move +=1

        if y+1<C and forest[x][y+1]!='X' and forest[x][y+1]!='*':
            if forest[x][y+1] == 'D':return 1
            forest[x][y+1] = 'S'
            hog.append((x,y+1))
    #         move +=1
    # if move == 0:
    #     return 2

days = 0
while True:
    days += 1
    water_bfs()
    # ans  = hog_bfs()
    if hog_bfs()==1:
        print(days)
        break
    # if ans==2:
    #     print('KAKTUS')
    #     break
    if len(hog)==0:
        print('KAKTUS')
        break
    
