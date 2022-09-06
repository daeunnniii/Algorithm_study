def solution(beginning, target):
    answer = 0
    for i in range(len(beginning)):
        if beginning[i][0] != target[i][0]:
            answer += 1
            for j in range(len(beginning[0])):
                if beginning[i][j] == 1:
                    beginning[i][j] = 0
                else:
                    beginning[i][j] = 1

    for j in range(len(beginning[0])):
        if beginning[0][j] != target[0][j]:
            answer += 1
            for i in range(len(beginning)):
                if beginning[i][j] == 1:
                    beginning[i][j] = 0
                else:
                    beginning[i][j] = 1
    if beginning!=target:
        return -1
    return answer

beginning = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
target = [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
print(solution(beginning, target))
print(solution([[0,0,0],[0,0,0],[0,0,0]], [[1,0,1],[0,0,0],[0,0,0]]))