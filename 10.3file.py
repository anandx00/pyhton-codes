
with open("guest.txt","w") as file_object:
    for times in range(10):
        name=input("enter your name guest")
        file_object.write(f'{name}\n')
file_object.close()
