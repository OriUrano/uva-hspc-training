n = int(input())
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
st = sum(a)
mx = st

for i in range(n):
    st += b[i] - a[i]
    mx = max(mx, st)

print(mx)