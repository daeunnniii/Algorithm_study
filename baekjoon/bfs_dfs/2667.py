import sys
sys.setrecursionlimit(10**6)
n = int(input())
count, neighbor, answer = 0, [], []
for _ in range(n):
    house = input()
    neighbor.append([int(h) for h in house])
def dfs(x, y):
    global count
    if x<0 or y<0 or x>=n or y>=n:
        return False
    if neighbor[y][x] == 1:
        count += 1
        neighbor[y][x] = 0
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False
for i in range(n):
    for j in range(n):
        count = 0
        if dfs(j, i) == True:
            answer.append(count)
print(len(answer))
answer.sort()
for a in answer:
    print(a)
