import sys
sys.setrecursionlimit(10**5)
read = sys.stdin.readline

n, m = map(int,read().rstrip().split())
# n개의 비어있는 리스트
line = [[] for _ in range(n+1)]
visited = [False]  * (n+1)


for _ in range(m):
    front, back = map(int,read().rstrip().split())
    line[back].append(front)


def dfs(line, node, visited):

    # 순서대로 돌건데, 이미 왔던 곳이면 return

    if visited[node] == True:
        return

    visited[node] = True

    # 앞에 있는 녀석 없어 or 몰라
    if not line[node]:
        print(node, end = " ")
        return

    # 내 앞에 있는 녀석들한테 들어간다.
    for front in line[node]:
        if visited[front] == False:
            # 온 적 없으면 들어간다.
            dfs(line,front,visited)
    # 나오면 본인 출력 -- 내 앞에 있어야 할 녀석들은 다 출력한거임
    print(node, end = " ")


for i in range(1,n+1):
    dfs(line,i,visited)