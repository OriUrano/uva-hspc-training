from collections import Counter

a = Counter(map(str, input().split()))
b = a.most_common()

c = []
for k,v in b:
    if v==b[0][1]:
        c.append(k)
    else:
        break

print(" ".join(c))
