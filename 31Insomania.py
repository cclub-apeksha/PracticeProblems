k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
a = []
for i in range(min(k,l,m,n), d+1):
    if i%k == 0 or i%l == 0 or i%m ==0 or i%n==0 not in a:
        a.append(i)
print(len(a))


