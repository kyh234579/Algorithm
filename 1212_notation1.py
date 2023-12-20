N,B = input().split()
arr="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N=N[::-1]
sum=0
for i, v in enumerate(N):
    sum+=(int(B) ** i) * arr.index(v)

print(sum)
