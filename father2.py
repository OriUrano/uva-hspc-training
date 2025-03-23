from collections import Counter

a = tuple(map(str, input().split()))
c = [k for k, v in Counter(a).items() if v > 1]

print(" ".join(c))