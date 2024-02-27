import random 
import string
userinput=int(input("choose 1 for encrypting message and 2 for reversing the message"))
if userinput==1:
    x=input("enter the message which you have to convert in secret language")
    list=[]
    for i in x:
        list.append(i)
        #print(list)
    if (len(list))<3:
        list.reverse()
        for i in list:
           print(i,end="")
    elif len(list) >=3:
        list.append(list[0])
        list.pop(0)
        #print(list)
    i=0
    while i<=2:
        z=random.choices(string.ascii_lowercase)
        k=random.choices(string.ascii_lowercase)
        list.append(z[0])
        list.insert(0,k[0])
        #print(list)
        i+=1
    for i in list:
        print(i,end="")
elif userinput==2:
    

    p=input("enter the message which you have to decode")
    list=[]
    if len(p)<3:
        for i in p:
            list.append(i)
        list.reverse()
        for i in list:
            print(i,end="")
    else:
        for i in p:
            list.append(i)
            print(list)
        i=0
        while i<=2:
            list.pop()
            list.pop(0)
            print(list)
            i+=1
        list.insert(0,list[-1])
        list.pop()
        for k in list:
            print(k,end="")

    
#print((random.choices(string.ascii_lowercase)))