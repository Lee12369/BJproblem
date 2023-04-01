B, C, D = map(int, input().split())
burger_menu = list(map(int, input().split()))
burger_menu.sort(reverse=True)

side_menu = list(map(int, input().split()))
side_menu.sort(reverse=True)

drink_menu = list(map(int, input().split()))
drink_menu.sort(reverse=True)

# 세트 메뉴를 만들 수 있는 최대 개수는 각 메뉴 종류의 개수 중 최소 개수만큼 가능하다.
N = min(len(burger_menu), len(side_menu), len(drink_menu))
before_sale_price = sum(burger_menu) + sum(side_menu) + sum(drink_menu)

sale_price = (sum(burger_menu[:N]) + sum(side_menu[:N]) + sum(drink_menu[:N])) // 10
after_sale_min_price = before_sale_price - sale_price

print(before_sale_price)
print(after_sale_min_price)
