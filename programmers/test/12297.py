def solution(X, Y):
    answer = []
    X = [i for i in X]
    Y = [j for j in Y]
    X.sort(reverse=True)
    Y.sort(reverse=True)
    point=0
    for x in X:
        while point<len(Y)-1 and x<Y[point]:
            point += 1
        if x==Y[point]:
            answer.append(x)
            point += 1
            if point > len(Y)-1:
                break
    if not answer:
        return "-1"
    if answer[0] == "0":
        return "0"
    return "".join(answer)