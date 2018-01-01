n= int(input())
a= sorted(list(map(int,input().split())))
b=s=0
while b<=sum(a):
    b+=a.pop()
    s+=1
print(s)


