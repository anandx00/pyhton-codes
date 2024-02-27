y=int(input("enter the range till you have to get prime number"))
for x in range(1,y+1):
    for i in range(2,x):
        if x%i==0:
            break
    else:
        print(f"{x}",end=" ,")