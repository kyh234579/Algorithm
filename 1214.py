a,b,c,d,e,f =map(int,input().split())

for i in range(-999,10000):
    for j in range(-999,10000):
        if a*i + b*j == c and c*i + d*j == f:
            print(i,j)
            break