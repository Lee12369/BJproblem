all_price = int(input())
price_list = [int(input()) for _ in range(9)]

sum_price = sum(price_list)

answer = all_price - sum_price

print(answer)