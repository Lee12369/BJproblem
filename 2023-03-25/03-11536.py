import sys
input = sys.stdin.readline

N = int(input())
names = [input() for _ in range(N)]

increasing_names = sorted(names)
decreasing_names = list(reversed(increasing_names))

if names == increasing_names:
    print("INCREASING")

elif names == decreasing_names:
    print("DECREASING")

else:
    print("NEITHER")

print(names)
print(increasing_names)
print(decreasing_names)
