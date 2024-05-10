w,h=map(int,input().split())
n=int(input())
stores=[list(map(int,input().split())) for _ in range(n)]
donguen=list(map(int,input().split()))
total=0
if donguen[0]==2:
    for store in stores:
        if store[0]==1:
            total+=min(store[1]+h+donguen[1],w-donguen[1]+h+w-store[1])   
        elif store[0]==2:
            total+=abs(store[1]-donguen[1])
        elif store[0]==3:
            total+=h-store[1]+donguen[1]
        elif store[0]==4:
            total+=h-store[1]+w-donguen[1]
elif donguen[0]==1:
    for store in stores:
        if store[0]==1:
            total+=abs(donguen[1]-store[1])
        elif store[0]==2:
            total+=min(donguen[1]+h+store[1],w-store[1]+h+w-donguen[1])
        elif store[0]==3:
            total+=store[1]+donguen[1]
        elif store[0]==4:
            total+=store[1]+w-donguen[1]
elif donguen[0]==3:
    for store in stores:
        if store[0]==1:
            total+=store[1]+donguen[1]
        elif store[0]==2:
            total+=store[1]+h-donguen[1]
        elif store[0]==3:
            total+=abs(donguen[1]-store[1])
        elif store[0]==4:
            total+=min(store[1]+w+donguen[1],h-donguen[1]+w+h-store[1])
elif donguen[0]==4:
    for store in stores:
        if store[0]==1:
            total+=w-store[1]+donguen[1]
        elif store[0]==2:
            total+=w-store[1]+h-donguen[1]
        elif store[0]==3:
            total+=min(store[1]+w+donguen[1],h-donguen[1]+w+h-store[1])
        elif store[0]==4:
            total+=abs(store[1]-donguen[1])
print(total)