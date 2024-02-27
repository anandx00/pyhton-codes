def sort(list):
    list=[34,3,4,5,4,5,3,43,24,3]

    for k in range (len(list)):
        for i in range(len(list)): 
            if i < len(list)-1:
                if list[i]>=list[i+1]:
                    list[i],list[i+1]=list[i+1],list[i]
    
    
    
    
    return list









print(sort(list))