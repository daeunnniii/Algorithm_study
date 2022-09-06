def binary_search(trees, m):
    result, start, end = 0, 0, max(trees)
    while start<=end:
        length = 0
        mid = (start+end)//2
        for t in trees:
            if t - mid > 0:
                length += t-mid
        if length >= m:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

n, m = map(int, input().split())
trees = list(map(int, input().split()))
print(binary_search(trees, m))