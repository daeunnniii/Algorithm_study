def solution(m, n, puddles):
    path = [[1]*m for _ in range(n)]
    for x, y in puddles:
        path[y-1][x-1] = 0
    for i in range(n):
        for j in range(m):
            if path[i][j] == 0:
                continue
            if i==0 and j==0:
                pass
            elif i==0 and j!=0:
                path[i][j] = path[i][j-1]
            elif i!=0 and j==0:
                path[i][j] = path[i-1][j]
            else:
                path[i][j] = path[i-1][j] + path[i][j-1]  
    return path[-1][-1]%1000000007