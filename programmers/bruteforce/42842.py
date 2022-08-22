import math
def solution(brown, yellow):
    answer = []
    yellow_divisor = [i for i in range(1, int(math.sqrt(yellow))+1) if yellow%i == 0]
    for y in yellow_divisor:
        x = yellow//y
        if brown == (2*x + 2*y + 4):
            answer.append(x+2)
            answer.append(y+2)
            break
    answer.sort(reverse=True)
    return answer