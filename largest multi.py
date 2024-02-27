def largest_product(series, size=5):
    anand=list(map(lambda x:int(x),series))
    empty=[]
    for i in range(len(series)-size+1):
        k=anand[i]
        for number in range(size-1):
            k*=anand[number +i+1]
        empty.append(k)
    empty.sort()
    return empty[-1]


    

