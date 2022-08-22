import itertools
import math
def isPrimeNumber(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers = [n for n in numbers]
    for i in range(1, len(numbers) + 1):
        permutation_lst = set(itertools.permutations(numbers, i))
        for p in permutation_lst:
            current_num = "".join(p)
            if current_num[0] == '0':
                continue
            else:
                if isPrimeNumber(int(current_num)) == True:
                    answer += 1
    return answer