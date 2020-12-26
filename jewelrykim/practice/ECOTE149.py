# 음료수 얼려먹기
import sys
import numpy as np
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/practice/149.txt", 'r')
ice_box =[]
N, M = map(int, sys.stdin.readline().split())

for _ in range(N):
    small_box = []
    row = sys.stdin.readline().rstrip()
    for ice in row:
        small_box.append(int(ice))
    ice_box.append(small_box)

ice_box = np.array(ice_box)
print(ice_box)
count = 0
def dfs(graph, i, j):
    global count
    if graph[i][j]==0:
        count += 1
        graph[i][j] = 1
        if i != N-1:clean_side(graph, i+1, j)
        elif j != M-1:clean_side(graph, i, j+1)
        elif i != 0:clean_side(graph, i -1, j)
        elif j != 0:clean_side(graph, i, j-1)
    else:
        return
def clean_side(graph, i, j):
    if graph[i][j]==0:
        graph[i][j]=1
        if i != N-1:clean_side(graph, i+1, j)
        elif j != M-1:clean_side(graph, i, j+1)
        elif i != 0:clean_side(graph, i -1, j)
        elif j != 0:clean_side(graph, i, j-1)
    else:
        return

for i in range(N):
    for j in range(M):
        dfs(ice_box, i, j)


print(count)
