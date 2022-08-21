def solution(s):
    answer = True
    check = []
    for c in s:
        if c == "(":
            check.append(1)
        else:
            if len(check)==0:
                answer = False
                break
            else:
                check.pop()
    if len(check)>0:
        answer = False
    return answer