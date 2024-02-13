n=int(input())
pt_list=list(map(int,input().split()))
pt_list.sort()
if n%2!=0:
    tmp=pt_list[-1]
    left=0
    right=n-2
    while left < right:
        tmp=max(tmp,pt_list[left]+pt_list[right])
        left+=1
        right-=1
    print(tmp)
else:
    tmp=0
    left=0
    right=n-1
    while left < right:
        tmp=max(tmp,pt_list[left]+pt_list[right])
        left+=1
        right-=1
    print(tmp)
