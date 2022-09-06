from datetime import datetime
import math
def solution(fees, records):
    carlist, answer = [], []
    for r in records:
        time, n, i_o =  r.split(' ')
        carlist.append([n, time])
    carlist.sort()
    while carlist:
        i, sum_t = 1, 0
        while i<len(carlist) and carlist[0][0] == carlist[i][0]:
            diff = datetime.strptime(carlist[i][1], "%H:%M") - datetime.strptime(carlist[i-1][1], "%H:%M")
            sum_t += diff.seconds//60
            i += 2
        if i<=len(carlist) and carlist[0][0] == carlist[i-1][0]:
            diff = datetime.strptime("23:59", "%H:%M") - datetime.strptime(carlist[i-1][1], "%H:%M")
            sum_t += diff.seconds//60
            i += 1
        if sum_t <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(math.ceil((sum_t - fees[0])/fees[2]) * fees[3] + fees[1])
        del carlist[:i-1]
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))