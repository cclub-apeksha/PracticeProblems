name = input()
a = []
for i in name:
    if i not in a :
        a.append(i)
if len(a)%2==0 :
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
print(a)
