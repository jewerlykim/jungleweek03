# 숨바꼭질 bfs로 풀거당 수빈이 위치에서 -1 +1   곱하기 2 할때마다 +1 
import sys
from collections import deque
# sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/practice/1697.txt",'r')

N, K = map(int, sys.stdin.readline().split())

x_axis = [0 for _ in range(100001)]
visited = [True for _ in range(100001)]

x_axis[N] = 0
x_axis[K] = -1


time_list = []
def bfs():
    queue = deque()
    queue.append((N,0))

    while queue:
        x,count = queue.popleft()
        plus = x + 1
        minus = x - 1
        multi = 2*x
        if x== K:
            return count
        
        if visited[x]:
            visited[x] = False
            if plus<100001:
                queue.append((plus,count+1))
            if 0<=minus:
                queue.append((minus,count+1))
            if multi<100001:
                queue.append((multi,count+1))


print(bfs())
