def slices(series, length):
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if len(series)==0:
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    k=[]
    for i in range(len(series)):
        if length+i == len(series)+1:
            break
        else:
            k.append(series[i:length+i])
    return k
print(slices("1234566",2))
        


        
