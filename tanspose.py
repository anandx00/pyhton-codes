def transpose(lines):
    
    expected=[]
    z=[] 
    for i in lines:
        if len(i)<len(max(lines)):
            i=i+" "*(len(max(lines))-len(i))
            z.append(i)
        else:
            z.append(i) 
    for i in range(len(z)):
        for k in range(len(z[i])):
            if i==0 :
                expected.append(z[i][k]) 
            else:
                expected[k]=expected[k]+z[i][k]                
    return '\n'.join(expected)
    


print(transpose(["The fourth line.","anand kumar'"]))

            
        
