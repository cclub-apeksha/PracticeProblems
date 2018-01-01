n = int(input())
accomodation = 0
for i in range(n):
    a, b = map(int, input().split())
    if b - a >= 2:
        accomodation += 1
print(accomodation)
