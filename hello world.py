import string
from time import sleep

hello=input("write the text")
match=string.ascii_lowercase +" "
hii=str()
for i in hello:
    for k in match:
        sleep(.02)
        if i!=k:
            print("\033[92m"+hii+k) #assi code for green
        else:
            hii=hii+i
            print("\033[92m"+hii)
            break


