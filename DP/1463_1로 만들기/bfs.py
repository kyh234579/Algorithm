from collections import deque
x=int(input())
visited=[0]*(x+1)
Q=deque([x])
while Q:
    c=Q.popleft()
    if c ==1:
        break
    if c%3==0 and visited[c//3]==0:
        Q.append(c//3)
        visited[c//3]=visited[c]+1
    if c%2==0 and visited[c//2]==0:
        Q.append(c//2)
        visited[c//2]=visited[c]+1
    if visited[c-1]==0:
        Q.append(c-1)
        visited[c-1]=visited[c]+1

print(visited[1])