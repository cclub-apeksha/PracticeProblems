input()
x=input()
count=0
for i in range(0,len(x)-1):
    if x[i]=='R' and x[i+1]=='R':
        count+=1
    elif x[i]=='G' and x[i+1]=='G':
        count+=1
    elif x[i]=='B' and x[i+1]=='B':
        count+=1
print(count)