def solution(today, terms, privacies):
    answer = []
    year,month,day=map(int,today.split('.'))
    today_sum=year*12*28+month*28+day
    for i in range(len(privacies)):
        date,t_type=privacies[i].split()
        d_year,d_month,d_day=map(int,date.split('.'))
        d_sum=d_year*12*28+d_month*28+d_day
        for term in terms:
            ttype,num=term.split()
            if t_type == ttype:
                if d_sum+int(num)*28 <= today_sum:
                    answer.append(i+1)
    return answer 