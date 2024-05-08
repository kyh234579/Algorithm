k=int(input())
#가로
width=[]
#세로
height=[]
total=[]
for _ in range(6):
    dir,length=map(int,input().split())
    #동서 -> 가로 리스트 추가
    if dir==1 or dir==2:
        width.append(length)
        total.append(length)
    else:
        height.append(length)
        total.append(length)

bigbox=max(width)*max(height)

maxhidx=total.index(max(height))
maxwidx=total.index(max(width))

if maxhidx==5:
    smallwidth=abs(total[maxhidx-1]-total[0])
else:
    smallwidth=abs(total[maxhidx-1]-total[maxhidx+1])

if maxwidx==5:
    smallheight=abs(total[maxwidx-1]-total[0])
else:
    smallheight=abs(total[maxwidx-1]-total[maxwidx+1])

res=bigbox-(smallheight*smallwidth)
print(res*k)
