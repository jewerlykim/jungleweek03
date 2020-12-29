from collections import deque
import sys
read = sys.stdin.readline

R, C = map(int,read().rstrip().split())
forest = []
queue_water = deque()
queue_hedgehog = deque()
hedgehog_count = 0
suc = False
# 상하좌우
dx = [1,-1,0,0]
dy = [0,0,-1,1]


# 연속으로 받을 때는 split()안하도록 주의하자!
for i in range(R):
    forest.append(list(read().rstrip()))

# 물, 고슴도치 찾기 !
for i in range(R):
    for j in range(C):
        if forest[i][j] == "*":
            queue_water.append((i,j))
        if forest[i][j] == "S":
            queue_hedgehog.append((i,j))
            # hedgehog_count += 1


def water_bfs(forest):
    # global hedgehog_count
    # global suc
    # hedgehog_count = len(queue_hedgehog)
    
    # 날짜가 지나면 끊어주는 것 추가
    len_water = len(queue_water)
    # 하루가 끝나는 조건
    while len_water > 0:
        
        # 날짜 종료 조건
        x,y = queue_water.popleft()
        len_water -= 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 경로 이탈 시
            if nx < 0 or nx >= R or ny <0 or ny >= C:
                continue
            
            # 돌이나 비버 집
            if forest[nx][ny] == "X" or forest[nx][ny] == "D":
                continue
            
            # 중간에 다 잡아 먹었으면
            # 고려하지 않았음... 
            # 물 바로 옆에 있으면 안됨
            # --> 해답 : 잡아먹혀도, 살아있다!!!!


            # 시작부터 옆에 있으면?
            # --> 해답 : 잡아먹혀도, 살아있따!!!!

            # 중복 넣지 않게 꼭 이 조건 추가!
            if forest[nx][ny] != "*":
                forest[nx][ny] = "*"
                queue_water.append((nx,ny))

# 바깥에 있는 sucess를 갖고오지말고,
# True 를 내보낸다.

def hedgehog_bfs(forest):
    # 성공 여부
    len_hedgehog = len(queue_hedgehog)

    while len_hedgehog > 0:
        
        x,y = queue_hedgehog.popleft()
        len_hedgehog -= 1

        # 더이상 전진할 수 없을 때 !
        # suc = "KAKTUS"
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 경로 이탈 시
            if nx < 0 or nx >= R or ny <0 or ny >= C:
                continue
            
            # 돌이나 물
            if forest[nx][ny] == "X" or forest[nx][ny] == "*":
                continue
            
            # 비버집 !
            if forest[nx][ny] == "D":
                return True

            # 중복 넣지 않게 꼭 이 조건 추가! -- 메모리 초과 원인
            # 물이었던것, 도치였던 것을 추가하지 않게끔
            if forest[nx][ny] == ".":
                forest[nx][ny] = "S"
                queue_hedgehog.append((nx,ny))



day = 0


# 잡아먹혀도 살아있는거임 !!!!!
while True:
    day += 1
    water_bfs(forest)
    if hedgehog_bfs(forest):
        print(day)
        break
    # success 하지 못하고, 0이면 KAKTUS다
    if len(queue_hedgehog) == 0:
        print("KAKTUS")
        break



                
    # if not queue_hedgehog:
    #     print("KAKTUS")
    #     break
