import sys
input = sys.stdin.readline
S,E,Q=input().split()
S=60*int(S[:2])+int(S[3:])
E=60*int(E[:2])+int(E[3:])
Q=60*int(Q[:2])+int(Q[3:])
arr=set()
tmp=0
while True:
    try:
        time,nickname=map(str,input().split())
        time=60*int(time[:2])+int(time[3:])
        if time <=S:
            arr.add(nickname)
        elif time>=E and time<=Q:
            if nickname in arr:
                tmp+=1
                arr.remove(nickname)
    except:
        break

print(tmp)
