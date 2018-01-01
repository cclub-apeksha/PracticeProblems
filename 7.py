count =0
ques = int(input())
for i in range (0,ques) :
    a,b,c = map(int,input().split())
    if a+b+c >=2 :
        count+= 1
print(count)