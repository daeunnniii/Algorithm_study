import bisect

n = int(input())
n_lst = list(map(int, input().split(' ')))
m = int(input())
m_lst = list(map(int, input().split(' ')))
n_lst.sort()

answer = []
for target in m_lst:
    l = bisect.bisect_left(n_lst, target)
    r = bisect.bisect_right(n_lst, target)
    answer.append(r - l)
for a in answer:
    print(a, end=' ')
