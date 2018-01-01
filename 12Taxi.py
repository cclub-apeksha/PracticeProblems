input()
a,b,c,d = map(input().split().count,['1','2','3','4'])
print(c+d+(max(a-c,0)+b*2 + 3)//4)


