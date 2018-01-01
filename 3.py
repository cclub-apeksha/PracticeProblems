iteration = int(input())
count = 0

while count < iteration :
    word = input()
    length = len(word)
    if length > 10 :
        print (word[0]  + str(length-2 ) + word[length -1] )
    else :
        print (word)
    count = count + 1
