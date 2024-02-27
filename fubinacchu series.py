x=int(input("enter a number of which you have to get series"))
l=[0,1]
for i in range(0,x-1):
    y=l[i]+l[i+1]
    l.append(y)
    print(l[-1])
if x==0:
    print(0)
