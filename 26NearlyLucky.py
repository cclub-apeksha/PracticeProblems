number = input()
a = []
for i in number:
    if i in ['4','7'] :
        a.append(i)
l = len(a)
if l in (4,7):
    print("YES")
else:
    print('NO')

print('YES' if sum(a in '47' for a in input()) in (4, 7) else 'NO')