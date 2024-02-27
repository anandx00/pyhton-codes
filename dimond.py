import string
def dimond(x):
    k=list(map(lambda x:x,string.ascii_uppercase))
    l=[]
    for i in range(k.index(x),-1,-1):
        for z in range(0,k.index(x)+1):
            if k.index(x)-i==z:
                if z==0:
                    l.append(i * " "+k[z]+i *" ")
                else:
                    l.append(i * " "+k[z]+z*2*" "+k[z] +i *" ")
    lambda x:l.append(x), reversed(l[:-1])
    for i in l:
        print(i)
    for i in reversed(l):
        print(i)
print(dimond('Z'))