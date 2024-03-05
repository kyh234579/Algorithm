import math
def solution(fees, records):
    answer = []
    dic={}
    arr=set()
    for record in records:
        time,car_num,info=record.split()
        arr.add(int(car_num))
    arr=sorted(arr)
    new_dict={}
    #오름차순 정렬
    for a in arr:
        new_dict[a]=0
    for record in records:
        time,car_num,info=record.split()
        if car_num not in dic.keys() and info == 'IN':
            dic[car_num]=time
        elif info =='OUT' and car_num in dic.keys():
            parking_time=(60*int(time[:2])+int(time[3:]))-(60*int(dic[car_num][:2])+int(dic[car_num][3:]))
            del dic[car_num]
            new_dict[int(car_num)]+=parking_time
    if dic:
        for key,value in dic.items():
            parking_time=(60*23+59)-(60*int(value[:2])+int(value[3:]))
            new_dict[int(key)]+=parking_time
                
    #요금 계산
    for parking_time in new_dict.values():
        if parking_time<=fees[0]:
            answer.append(fees[1])
            continue
        ssum=fees[1]+math.ceil((parking_time-fees[0])/fees[2])*fees[3]
        answer.append(ssum)
    
    return answer