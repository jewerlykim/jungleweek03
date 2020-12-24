import sys

R, C = map(int, sys.stdin.readline().split())
li = []
for _ in range(R):
    li.append(list(sys.stdin.readline().rstrip()))


def alphabet(graph, x, y):
    visited = []
    stack = [[x, y]]
    maxi = 0

    while stack:
        top = stack.pop()
        x, y = top[0], top[1]

        if graph[x][y] not in visited:
            visited.append(graph[x][y])
            if x - 1 >= 0:
                stack.append([x - 1, y])
            if x + 1 < R:
                stack.append([x + 1, y])
            if y - 1 >= 0:
                stack.append([x, y - 1])
            if y + 1 < C:
                stack.append([x, y + 1])

        maxi = max(maxi, len(visited))

    return maxi


print(alphabet(li, 0, 0))
