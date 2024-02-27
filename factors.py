
def factor(value):
    l=[]
    for i in range(int(value/2 +1)):
        for k in reversed(range(value)):
            if i*k == value:
                l.append(i)
                value=int(value/i)
    return(l)