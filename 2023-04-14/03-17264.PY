N, P = map(int, input().split())
W, L, G = map(int, input().split())

win_players = []
for _ in range(P):
    player, win_or_lose = input().split()
    if win_or_lose == 'W':
        win_players.append(player)

with_players = [input() for _ in range(N)]

iron_man = True
score = 0
for player in with_players:
    if player in win_players:
        score += W
    else:
        score -= L

    if score >= G:
        iron_man = False
        break

    if score < 0:
        score = 0

if iron_man == True:
    print("I AM IRONMAN!!")
else:
    print("I AM NOT IRONMAN!!")

