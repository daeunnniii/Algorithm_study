def solution(triangle):
    mem = []
    mem.append(triangle[0][0])
    for t in range(1, len(triangle)):
        current_mem = [0 for _ in range(t+1)]
        for s in range(len(triangle[t])):
            if s==0:    
                current_mem[s] = mem[s] + triangle[t][s]
            elif s==len(triangle[t])-1:
                current_mem[s] = mem[s-1] + triangle[t][s]
            else:
                current_mem[s] = max(mem[s-1] + triangle[t][s], (mem[s] + triangle[t][s]))
        mem = list(current_mem)
    return max(mem)