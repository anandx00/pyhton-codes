def label(colors):
    k=['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    m=""
    for i in range(3):
        if i==2:
            m+=f"{'0'*k.index(colors[i])}"
        else:
            m+=str(k.index(colors[i]))
    z = list(map(lambda x:x ,m))
    if z.count('0')<=2:
        return str(int(m))+' ohms'
    elif z.count('0')<=5 and z.count('0') >2:
        return str(int(m)//10**3 )+' kiloohms'
    elif z.count('0')<=8 and z.count('0') >5:
        return str(int(m)//10**6 )+' megaohms'
    elif z.count('0')<=11 and z.count('0') >8:
        return str(int(m)//10**9 )+' gigaohms'
    elif z.count('0')<=14 and z.count('0') >11:
        return str(int(m)//10**12 )+' teraohms'
    elif z.count('0')<=17 and z.count('0') >14:
        return str(int(m)//10**15 )+' petaohms'

    
    
    
    
    
print(label(["red", "black", "red"]))