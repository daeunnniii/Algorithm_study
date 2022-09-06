n, k = map(int, input().split(' '))
lst = [1000000] * 200000
lst[n] = 0
for i in [n-1, n+1, 2*n]:
    lst[i] = 1
print(f'n: {n}, lst[:k+1]: {lst[:k+1]}')
while n <= 2*k:
    n += 1
    lst[n-1] = min(lst[n-2]+1, lst[n]+1, lst[n-1])
    lst[n+1] = min(lst[n]+1, lst[n+1])
    lst[2*n] = min(lst[n]+1, lst[2*n])
    print(f'n: {n}, lst[:k+1]: {lst[:k+1]}')
print(lst[k])