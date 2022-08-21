from collections import deque
def solution(arr):
    answer = []
    arr = deque(arr)
    answer.append(arr.popleft())
    while arr:
        p = arr.popleft()
        if answer[-1] != p:
            answer.append(p)
    return answer