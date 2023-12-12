n=int(input())
village=[]
allPeople=0
for i in range(n):
    x,a=map(int,input().split())
    village.append([x,a])
    allPeople+=a

village.sort(key=lambda x:x[0])
cnt=0
for i in range(len(village)):
    cnt+=village[i][1]
    if cnt >= allPeople/2:
        print(village[i][0])
        break

