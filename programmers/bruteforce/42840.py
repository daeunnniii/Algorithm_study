def solution(answers):
    first_std = [1, 2, 3, 4, 5]
    second_std = [2, 1, 2, 3, 2, 4, 2, 5]
    third_std = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == first_std[i%5]:
            score[0] += 1
        if answers[i] == second_std[i%8]:
            score[1] += 1
        if answers[i] == third_std[i%10]:
            score[2] += 1
    max_score = max(score)
    if score.count(max_score) > 1:
        result = [i+1 for i in range(len(score)) if score[i] == max_score]
    else:
        result = [score.index(max_score)+1]
    return result