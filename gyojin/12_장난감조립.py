import sys

sys.stdin = open('../co_coding/input.txt', 'r')
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
toy = [[] for _ in range(N+1)]
for _ in range(M):
    X, Y, K = map(int, sys.stdin.readline().split())
    toy[X].append([Y, K])

print(toy)
