import os
import random 
def rename():
    k=os.listdir()
    m=0
    for i in k:
        if i.endswith('.png'):
            os.rename(i,f'{m}.png')
            m+=1
            
