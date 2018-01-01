n, m = map(int, input().split())
f = 1001
a = sorted(list(map(int, input().split())))
for i in range(m-n+1):
    f = min(abs(a[i] - a[i + n - 1]), f)
print(f)


