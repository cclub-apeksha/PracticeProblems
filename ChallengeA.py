t = int(input())
for i in range(t):
    n = int(input())
    if n%3 == 0 or n%7 == 0:
        n = 0
    while(n>7):
        n = n-7
        if n%3==0 :
            n = 0
    if n == 0:
        print("YES")
    else:
        print("NO")
