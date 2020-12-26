# 음료수 얼려먹기
import sys
import numpy as np
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/practice/149.txt", 'r')
ice_box =[]
N, M = map(int, sys.stdin.readline().split())

for _ in range(N):
    ice_box.append(list(map(int, sys.stdin.readline().rstrip())))

ice_box = np.array(ice_box)


def dfs(x, y):
    # 주어진 범위를 벗어나느 경우에는 즉시 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    # 현재노드를 아직 방문하지 않았다면
    if ice_box[x][y] == 0:
        # 해당 노드 방문 처리
            ice_box[x][y] = 1
            # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x, y+1)
            return True
    return False

count = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            count += 1


print(count)
