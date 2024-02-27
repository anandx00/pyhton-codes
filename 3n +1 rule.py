
number=int(input("enter a number   "))
k=number
for i in range(10000):
    if k==1:
        break
    
    elif k %2 ==0:
        k=k//2
        print(k)
    else:
        k=k * 3 +1
        print(k)