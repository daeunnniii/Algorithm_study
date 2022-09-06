from itertools import permutations

def solution(k, dungeons):
    result = 0
    nPr = permutations(dungeons, len(dungeons))
    for p in nPr:
        power = k
        adventure = 0
        for l, s in p:
            if l <= power and power-s>=0:
                adventure += 1
                power -= s
            else:
                break
        if result < adventure:
            result = adventure  
    return result