x=0
n = int(input())
for i in range (0,n):
    a = list(input())
    for j in a:
        if j=='+':
            x+=1
            break
        elif j=='-':
            x-=1
            break
print(x)


