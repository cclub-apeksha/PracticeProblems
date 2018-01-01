cap = mcap = 0
n = int(input())
for i in range(n) :
    ex,en = map(int,input().split())
    cap+= en-ex
    mcap = max(mcap,cap)
print(mcap)

