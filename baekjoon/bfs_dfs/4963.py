import sys
sys.setrecursionlimit(100000)

answer = []
w, h = map(int, input().split(' '))
while w and h:
    result, maps = 0, []
    for i in range(h):
        maps.append(list(map(int, input().split(' '))))
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    def dfs(x, y):
        if x<0 or x>=w or y<0 or y>=h:
            return False
        if maps[y][x] == 1:
            maps[y][x] = 0
            for i in range(8):
                dfs(x+dx[i], y+dy[i])
            return True
        return False
    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(j, i) == True:
                result += 1
    answer.append(result)
    w, h = list(map(int, input().split(' ')))
for a in answer:
    print(a)