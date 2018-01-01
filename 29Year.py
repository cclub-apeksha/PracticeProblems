year = int(input())
new = year + 1
while len(set([i for i in str(new)]))!=4:
    new+=1
print(new)