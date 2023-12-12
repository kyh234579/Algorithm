N,B = map(int,input().split())
arr="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s=''
while N:
    s+=str(arr[N%B])
    N //= B

s=s[::-1]
print(s)






