from collections import Counter

a = tuple(map(int, input().split()))
c = Counter(a).most_common()[0][0]

print(c)