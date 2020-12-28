# 알파벳
import sys
sys.stdin = open('/Users/jewerlykim/Desktop/python_Algorithm/jungleweek03/jewelrykim/7.txt', 'r')


R, C = map(int, sys.stdin.readline().split())
alpha = []
visited = [False] * 27
for _ in range(R):
    alpha.append(list(map(str, sys.stdin.readline().rstrip())))
count = 0
count_list = []
def dfs(x,y):
    global count
    if x<=-1 or x>= R or y<=-1 or y>=C:
        return False
    if visited[ord(alpha[x][y])-64]==False:
        visited[ord(alpha[x][y])-64] = True
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        count += 1
        return True
    count_list.append(count)

    return False

dfs(0,0)
print(count_list)
print(count)

