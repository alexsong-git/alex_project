a = [1,2,3,4,5,6,7,8,9]
b = [1,2,3,4,5,6,7,8,9]

for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,' ',end='')
    print()