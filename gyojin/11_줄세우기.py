import sys
N, M = map(int, sys.stdin.readline().split())
li = []
stu = [[] for _ in range(N+1)]
for _ in range(M):
    key, value = map(int, sys.stdin.readline().split())
    li.append([key, value])


def line_up(graph):
    stack = []
    indegree = [0] * (N+1)
    ans = []

    for st, en in graph:
        indegree[en] += 1
        stu[st].append(en)
    # print('학생배열:', stu)
    # print('인덱스배열:', indegree)

    for i in range(1, N+1):
        if indegree[i] == 0:
            stack.append(i)
    # print('스택:', stack)

    while stack:
        node = stack.pop()
        # print('pop한 node:', node)
        ans.append(node)
        for i in stu[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                stack.append(i)
            # print('after 스택:', stack)
            # print('after 인덱스배열:', indegree)

    return ans


print(*line_up(li))
