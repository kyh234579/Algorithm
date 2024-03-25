#1이상 n이하로 바꿔서, k개 자릿수, 최대p개까지 반전 가능, 현재 층수 x
n,k,p,x=map(int,input().split())

num=[]
num.append([1,1,1,0,1,1,1])
num.append([0,0,1,0,0,1,0])
num.append([1,0,1,1,1,0,1])
num.append([1,0,1,1,0,1,1])
num.append([0,1,1,1,0,1,0])
num.append([1,1,0,1,0,1,1])
num.append([1,1,0,1,1,1,1])
num.append([1,0,1,0,0,1,0])
num.append([1,1,1,1,1,1,1])
num.append([1,1,1,1,0,1,1])

#자릿수 맞추기
if k>len(str(x)):
    cx='0'*(k-len(str(x)))+str(x)
else:
    cx=str(x)

#0~9까지 각 숫자가 반전시킬수 있는 LED갯수 구하기
#arr[i][j] -> i부터 j로 반전시킬수있는 led 갯수
arr=[]
for i in range(10):
    arr.append([])
    for j in range(10):
        if i==j:
            arr[i].append(0)
        else:
            d=0
            for h in range(7):
                if num[i][h] != num[j][h]:
                    d+=1
            arr[i].append(d)
            
#현재 idx, 남은 반전 가능 갯수, 현재 층수
def dfs(dep,cnt,cx):
    if dep==len(cx):
        #현재 층수와 같지않고, 1이상n이하라는 조건이 충족되면 갯수 count해주기
        if int(cx)!=x and 1<=int(cx)<=n:
            return 1
        else:
            return 0
        
    result,cur=0,int(cx[dep])
    for i in range(10):
        if cur!=i and arr[cur][i]<=cnt:
            dx=cx[:dep]+str(i)+cx[dep+1:]
            result+=dfs(dep+1,cnt-arr[cur][i],dx)

        #같으면
        elif cur==i:
            #위과정 생략하고, 다음 인덱스로 넘어가기
            result+=dfs(dep+1,cnt,cx)

    return result

print(dfs(0,p,cx))