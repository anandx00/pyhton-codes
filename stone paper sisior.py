# stone paper sisior 
import random
l=[1,2,3]
y=int(input('enter the number rounds you have to play'))
your_score=0
computer_score=0
for i in range(0,y):
    x=int(input('''1 for stone \n2 for paper \n3 for sisior\n'''))
    computer=random.choice(l)
    if computer ==1 :
        if computer==1 and x==3:
            computer_score+=1
            print ('you lost')
        elif computer == x:
            print ("draw")
        else:
            your_score+=1
            print('you win')
    if computer ==2 :
        if computer==2 and x==1:
            computer_score+=1
            print ('you lost')
        elif computer == x:
            print ("draw")
        else:
            your_score+=1
            print('you win')
    if computer ==3 :
        if computer==3 and x==2:
            computer_score+=1
            print ('you lost')
        elif computer == x:
            print ("draw")
        else:
            your_score+=1
            print('you win')
print(f"score are your score is = {your_score} \ncomputer score is = {computer_score} ")
print('no_one wins')if your_score == computer_score else print('you win the all round') if your_score > computer_score else print("computer wins") 

