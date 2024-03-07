n=int(input())
m=int(input())
s=input().rstrip()
left,right=0,0
answer=0

while right < m:
    if s[right:right+3]=='IOI':
        right+=2
        if right-left == 2*n:
            answer+=1
            left+=2
    else:
        left=right=right+1

print(answer)