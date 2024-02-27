data=[1,2,3,4,5,6,7,8,9,10]
element=int(input("enter the number which you have to search for"))
def search(data,element):
    for i in data:
        if element ==i:
            return ("the element is present in the list at index",data.index(element))
    else:
        return ("no such element is present")
print(search(data,element))