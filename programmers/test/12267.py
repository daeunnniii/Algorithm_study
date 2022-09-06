from collections import deque
def solution(order):
    i, answer, len_o = 1, 0, len(order)
    container = deque([])
    order = deque(order)
    while order:
        if i == order[0]:
            order.popleft()
            answer += 1
            i += 1
        elif container and container[-1] == order[0]:
            container.pop()
            order.popleft()
            answer += 1
        elif i<=len_o:
            container.append(i)
            i += 1
        else:
            break
    return answer

print(solution([4, 5, 3, 7, 8, 6, 2, 1]))