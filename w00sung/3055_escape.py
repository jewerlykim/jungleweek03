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
            hedgehog_count += 1


def water_bfs(forest):
    # global hedgehog_count
    # global suc
    # hedgehog_count = len(queue_hedgehog)
    
    # 날짜가 지나면 끊어주는 것 추가
    max_cnt = len(queue_water)
    cnt = 0
    while queue_water:
        
        # 날짜 종료 조건
        x,y = queue_water.popleft()
        cnt += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 경로 이탈 시
            if nx < 0 or nx >= R or ny <0 or ny >= C:
                continue
            
            # 돌이나 비버 집
            if forest[nx][ny] == "X" or forest[nx][ny] == "D":
                continue
            
            ## 물이 비버 잡아먹으면 ?! 
            # 개수 줄여주기
            # if forest[nx][ny] == "S":
            #     hedgehog_count -= 1

            # 중간에 다 잡아 먹었으면
            # 고려하지 않았음... 
            # 물 바로 옆에 있으면 안됨


            # 시작부터 옆에 있으면?
            # if hedgehog_count == 0:
            #     suc = "KAKTUS"
            #     return

            # 중복 넣지 않게 꼭 이 조건 추가!
            if forest[nx][ny] != "*":
                forest[nx][ny] = "*"
                queue_water.append((nx,ny))

            
        
        # 하루가 끝났습니다.
        if cnt == max_cnt:
            return


def hedgehog_bfs(forest):
    # 성공 여부
    global suc
    move = 0
    max_cnt = len(queue_hedgehog)
    cnt = 0

    while queue_hedgehog:
        
        x,y = queue_hedgehog.popleft()
        cnt += 1

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
                suc = True
                return suc

            # 중복 넣지 않게 꼭 이 조건 추가! -- 메모리 초과 원인
            if forest[nx][ny] == ".":
                forest[nx][ny] = "S"
                queue_hedgehog.append((nx,ny))
                move += 1
            

        # 하루가 끝났습니다.
        if cnt == max_cnt:
            #모든 hedgehog가 돌 or 물에 갇힘
            if move == 0:
                suc = "KAKTUS"

            return suc


suc = False
day = 0

while suc == False:
    water_bfs(forest)
    suc = hedgehog_bfs(forest)
    day += 1


if suc == True:
    print(day)
elif suc == "KAKTUS":
    print("KAKTUS")

                
    # if not queue_hedgehog:
    #     print("KAKTUS")
    #     break
