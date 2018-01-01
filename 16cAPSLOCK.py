s = str(input())
l = len(s)
if s[0].islower() and s[1:].isupper():
    print(''.join(s[0].upper()+s[1:].lower()))
elif s.isupper():
    print(s.lower())
elif l == 1 :
    print(s.upper())
else :
    print(s)

