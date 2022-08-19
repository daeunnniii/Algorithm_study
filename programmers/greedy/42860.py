def solution(name):
    min_move = len(name) - 1
    answer = 0
    for i, char in enumerate(name):
        answer += min(ord(char) - 65, 90 - ord(char) + 1)
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])
    answer += min_move
    return answer