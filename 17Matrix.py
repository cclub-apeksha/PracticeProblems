for i in range(0,5):
    a=input().split()
    if '1' in a:
        ans = abs(i-2) + abs(a.index('1')-2)
print(ans)
print(a)