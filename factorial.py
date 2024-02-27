
x=int(input("enter the number which you have to create a factorial++"))
for i in range(1,x):
    if x>0:
        x*=i
    else:
        print(1)
        break
print(x)
