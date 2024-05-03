n,m,b=map(int,input().split())
maps=[]
min_height=257
max_height=-1
min_time=1e9
height=-1
for _ in range(n):
    tmp=list(map(int,input().split()))
    maps.append(tmp)
for i in range(n):
    for j in range(m):
        if maps[i][j]<min_height:
            min_height=maps[i][j]
        if maps[i][j]>max_height:
            max_height=maps[i][j]
if min_height==max_height:
    print(0,min_height)
    exit()
for h in range(min_height,max_height+1):
    currentTime=0
    currentBlock=b
    for i in range(n):
        for j in range(m):
            current=maps[i][j]
            if h>current:
                gap=h-current
                currentTime+=gap
                currentBlock-=gap
            elif h<current:
                gap=current-h
                currentTime+=gap*2
                currentBlock+=gap
    if currentBlock<0:
        continue
    if min_time>currentTime:
        min_time=currentTime
        height=h
    elif min_time==currentTime and height<h:
        height=h

print(min_time,height)

        
                

