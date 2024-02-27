number=int(input("enter a number    : "))
def is_armstrong_number(number):
    k=str(number)
    z=len(k)
    y=0
    m=[]
    for i in k:
        m.append(int(i))
    for i in range(0,len(m)):
        y+=(m[i])**z
    if number ==y:
        print("number is a ")
    else:
        print("number is nnot")

is_armstrong_number(number)