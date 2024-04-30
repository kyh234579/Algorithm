from collections import deque
w,h=map(int,input().split())
graph=[[0]*(w+2) for _ in range(h+2)]
visited=[[False]*(w+2) for _ in range(h+2)]
for i in range(1,h+1):
    graph[i][1:w+1] = list(map(int,input().split()))

#홀수/ 왼쪽, 오른쪽, 아래, 아래 오른쪽, 위, 위 오른쪽
odd_dx=[-1,1,0,1,0,1]
odd_dy=[0,0,1,1,-1,-1]
#짝수/ 왼쪽, 오른쪽, 아래, 아래 오른쪽, 위, 위 오른쪽
even_dx=[-1,1,-1,0,-1,0]
even_dy=[0,0,1,1,-1,-1]

q=deque()
q.append((0,0))
result =0 
visited[0][0]=True

while q:
    y,x=q.popleft()
    #짝수라면
    if y%2==0:
        for i in range(6):
            ny=y+even_dy[i]
            nx=x+even_dx[i]
            if ny <0 or ny >= h+2 or nx <0 or nx>=w+2:
                continue
            #0과 1이 만나는 면이 벽면이 됨
            if graph[ny][nx] == 1:
                result+=1
            elif graph[ny][nx]==0 and not visited[ny][nx]:
                q.append((ny,nx))
                visited[ny][nx]=True
    #홀수
    else:
        for i in range(6):
            ny=y+odd_dy[i]
            nx=x+odd_dx[i]
            if ny <0 or ny >= h+2 or nx <0 or nx>=w+2:
                continue
            #0과 1이 만나는 면이 벽면의 길이가 됨
            if graph[ny][nx] == 1:
                result+=1
            elif graph[ny][nx]==0 and not visited[ny][nx]:
                q.append((ny,nx))
                visited[ny][nx]=True

print(result)


