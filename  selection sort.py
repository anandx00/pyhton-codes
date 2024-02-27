list=[1,2,45,76,74,53,0]

def selection_sort(list):

    for k in range(len(list)-1):
        min=k
        for i in range(k+1,len(list)):
            
            if list[i]<list[min]:
                min=i
    
        list[k],list[min]=list[min],list[k]
    return list
        
print(selection_sort(list))
