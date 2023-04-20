N, M = map(int, input().split())
problem_score = list(map(int, input().split()))

arr_answers =  [list(input().split()) for _ in range(M)]
arr_answers.sort(key=lambda x:int(x[0]))

max_score = 0
max_id = arr_answers[0][0]
for lst in arr_answers:
    id = lst[0]
    OX = lst[1:]

    score = 0
    for i in range(len(OX)):
        if OX[i] == 'O':
            score += problem_score[i]

    if score > max_score:
        max_score = score
        max_id = id

print(max_id, max_score)