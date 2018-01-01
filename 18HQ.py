print('YES' if set('HQ9').intersection(input()) else 'NO')
s=input()
if ("H" in s or "Q" in s or "9" in s):
    print("YES")
else:
    print("NO")