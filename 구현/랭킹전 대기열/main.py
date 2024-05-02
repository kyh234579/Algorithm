p,m=map(int,input().split())
rooms=[]
for _ in range(p):
    level,nick=map(str,input().split())
    level=int(level)
    flag=False
    for room in rooms:
        key=room[0][0]
        if len(room)<m:
            if key-10<=level<=key+10:
                room.append((level,nick))
                flag=True
                break
    if not flag:
        rooms.append([(level,nick)])
for room in rooms:
    if len(room)==m:
        print('Started!')
    else:
        print('Waiting!')
    room.sort(key=lambda x:x[1])
    for l,n in room:
        print(l,n)

    
