W_univ = [int(input()) for _ in range(10)]
K_univ = [int(input()) for _ in range(10)]

W_univ.sort(reverse=True)
K_univ.sort(reverse=True)

W_score = sum(W_univ[:3])
K_score = sum(K_univ[:3])

print(W_score, K_score)
