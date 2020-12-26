import sys
read= sys.stdin.readline

n_comp= int(read())
n_line = int(read())
graph = [[] for _ in range(n_comp+1)]


# 연결 설정
for _ in range(n_line):
    comp1, comp2 = map(int,read().rstrip().split())
    graph[comp1].append(comp2)
    graph[comp2].append(comp1)
    
visited = [False] * (n_comp+1)

cnt = -1
def dfs(graph,strt,visited):

    global cnt
    # 방문 처리시 + 1
    visited[strt] = True
    cnt += 1

    for i in graph[strt]:
        if visited[i] == False:
            dfs(graph,i,visited)

dfs(graph,1,visited)

print(cnt)