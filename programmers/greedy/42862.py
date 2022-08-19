def solution(n, lost, reserve):
    nobody_lend = []
    lost_lst = list(lost)
    
    for l in lost:
        if l in reserve:
            lost_lst.remove(l)
            reserve.remove(l)
            
    reserve.sort()
    lost_lst.sort()
    
    for l in lost_lst:
        if l-1 in reserve:
            reserve.remove(l-1)
        elif l+1 in reserve:
            reserve.remove(l+1)
        else:
            nobody_lend.append(l)
    answer = n - len(nobody_lend)
    return answer