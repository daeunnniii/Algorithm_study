def solution(N, number):
    store = [set([0]) if i==0 else set([int(str(N)*i)]) for i in range(9)]
    for a in range(2, 9):
        for b in range(1, a):
            for x in store[b]:
                for y in store[a-b]:
                    store[a].add(x+y)
                    store[a].add(x*y)
                    if x-y > 0:
                        store[a].add(x-y)
                    if x/y - int(x/y) == 0:
                        store[a].add(int(x/y))
    for i in range(len(store)):
        if number in store[i]:
            return i
    return -1
