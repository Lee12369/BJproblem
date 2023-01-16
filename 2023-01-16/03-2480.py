A, B, C = map(int,input().split())
if A == B == C:
    print("{}".format(10000 + A * 1000))
elif A == B or A == C:
    print("{}".format(1000 + A * 100))
elif B == C:
    print("{}".format(1000 + B * 100))
else:
    print("{}".format(max([A, B, C]) * 100))
