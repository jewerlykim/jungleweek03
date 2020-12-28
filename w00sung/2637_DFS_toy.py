import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

N = int(read())
M = int(read())

brick = [ [] for _ in range (N+1) ]
res = [0] * (N+1)
# middle_strt = float('inf')
for _ in range(M):

    main, sub, sub_piece = map(int,read().rstrip().split())
    # 중간 제품 or 완제품 처리
    if res[main] != -1:
        res[main] = -1
    # 필요한 요소들 연결 brick
    # O(1)
    brick[main].append((sub,sub_piece))

def dfs(main,piece):

    # 기본 제품이면,
    if not brick[main]:
        res[main] += piece
        return

    # 필요한 녀석들에게 들어감
    for needs in brick[main]:

        sub, sub_piece = needs
        
        dfs(sub,sub_piece*piece)

# N이다... not main
dfs(N,1)
# O(N)
for i in range(1,N+1):
    # res에는 기본제품만 저장된다.
    # O(1)
    if res[i] != -1:
        print(i, res[i])

# print(res)