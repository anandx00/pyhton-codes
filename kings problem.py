number=int(input("enter a number"))
def square(number):
    if number ==1 :
        return 1
    elif number <= 0:
        raise ValueError("square must be between 1 and 64")
    else:
        return 2**(number-1)
        


def total():
    if number==1:
        return 1
    else:
        return 2**(number-1)+ 2**(number -2)
print(total())