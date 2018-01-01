s = input()
t = input()
for i in s :
    translation = s[::-1]
if translation == t:
    print('YES')
else:
    print('NO')