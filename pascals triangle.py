
x=int(input("enter a number till you have to print pascal triangle"))

k=[]
for i in range(0,x):
    temp_list=[]
    for m in range(0,i+1):
        if m==0 or m==i:
            temp_list.append(1)
        else:
            temp_list.append(k[i-1][m-1]+k[i-1][m])
    k.append(temp_list)
print(k)
for i in range(0,10,-1):
    
    for i in k:
        print(i)