def solution(number, k):
    st = []
    for i in range(len(number)):
        print("k: ", k)
        while st and k > 0 and st[-1] < number[i]:
            st.pop()
            k -= 1
        st.append(number[i])
        print("number[i]: ", number[i])
        print("st: ", st)
    print("result:", st)
    return ''.join(st[:len(st) - k])    # 슬라이싱하는 이유는 6666과 같이 다 같은 숫자일 때 처리
