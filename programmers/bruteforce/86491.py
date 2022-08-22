def solution(sizes):
    sizes = [(a, b) if a>=b else (b, a) for a, b in sizes]
    width = max(sizes, key=lambda x:x[0])[0]
    height = max(sizes, key=lambda x:x[1])[1]
    return width*height