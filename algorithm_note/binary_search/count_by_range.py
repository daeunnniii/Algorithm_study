from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
# 값이 4인 데이터 개수 반환
count1 = count_by_range(a, 4, 4)
# 값이 [-1, 3] 범위에 있는 데이터 개수 반환
count2 = count_by_range(a, -1, 3)

for c in [count1, count2]:
    if c == 0:
        print(-1)
    else:
        print(c)