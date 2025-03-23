n = int(input())
a = list(map(int, input()))

for i in range(n-1):
    if a[i] == 0:
        a[i] = 1
        a[i+1] = 1 - a[i+1]

print("".join(map(str, a)))
