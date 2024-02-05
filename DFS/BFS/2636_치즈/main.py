from collections import deque
n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
visited=[[False]*m for _ in range(n)]

#총 시간 
total_time=0

#가장자리 녹은 치즈의 양
cheese_cnt=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

q=deque()
q.append((0,0))
visited[0][0]=True

while True:
    #녹일 치즈 가장자리 위치, 초기화 및 저장
    loc=set()
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny>=m:
                continue
            if board[nx][ny]==1:
                loc.add((nx,ny))
            elif board[nx][ny]==0 and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny]=True

    #더이상 녹일 치즈가 없으면 
    if not len(loc):
        print(total_time)
        break
    #가장자리 치즈 q에 넣어주고, 0으로 설정
    for i in loc:
        q.append((i[0],i[1]))
        board[i[0]][i[1]]=0
    total_time+=1
    cheese_cnt.append(len(loc))

print(cheese_cnt[-1])