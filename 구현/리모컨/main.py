n=input().rstrip()
m=int(input())
fix_button=list(map(int,input().split()))

if n==100:
    print(0)
    exit()

result=0
case=''
for i in range(len(n)):
    min_value=1e9
    for j in range(10):
        if n[i] in fix_button and abs(j-n[i]) < min_value:
            s1=j
        if j in fix_button:
            continue
        if n[i] == j:
            result+=1
            case+=str(j)
            break
    if n[i] in fix_button:
        result+=1
        case+=str(s1)

if case and int(case)<int(n):
    for i in range(int(case),int(n)+1):
        result+=1
elif case and int(case)>int(n):
    for i in range(int(n),int(case)+1):
        result+=1

print(result)
         
