#create a program capable of dispaling question to user like kbc
#use list data type to store the question and their correct answers
#dispaly the final amaint the person is taking home after playing the game.
question=['''Grand Central Terminal, Park Avenue, New York is the world's\n
1.	largest railway station
2.	highest railway station
3.	longest railway station
4.	None of the above''',
'''Entomology is the science that studies
1.	Behavior of human beings
2.	Insects
3.	The origin and history of technical and scientific terms
4.	The formation of rocks''',
'''Eritrea, which became the 182nd member of the UN in 1993, is in the continent of
1.	Asia
2.	Africa
3.	Europe
4.	Australia''','''	
Garampani sanctuary is located at
1.	Junagarh, Gujarat
2.	Diphu, Assam
3.	Kohima, Nagaland
4.	Gangtok, Sikkim''',
'''For which of the following disciplines is Nobel Prize awarded?
1.	Physics and Chemistry
2.	Physiology or Medicine
3.	Literature, Peace and Economics
4.	All of the above''',
'''Hitler party which came into power in 1933 is known as
1.	Labour Party
2.	Nazi Party
3.	Ku-Klux-Klan
4.	Democratic Party''',
'''FFC stands for
1.	Foreign Finance Corporation
2.	Film Finance Corporation
3.	Federation of Football Council
4.	None of the above''',
'''Fastest shorthand writer was
1.	Dr. G. D. Bist
2.	J.R.D. Tata
3.	J.M. Tagore
4.	Khudada Khan''',
'''Epsom (England) is the place associated with
1.	Horse racing
2.	Polo
3.	Shooting
4.	Snooker''',	
'''First human heart transplant operation conducted by Dr. Christiaan Barnard on Louis Washkansky, was conducted in
1.	1967
2.	1968
3.	1958
4.	1922''']
print('''if you want to 
add press 1
play kbc press 2
''')
pricelist=(1000,2000,3000,5000,10000,20000,40000,80000,160000,3200000)
answer=[1,2,2,2,4,2,2,1,1,1]
k=int(input())
if k==1:
    addquestion=input("write a question which you have to add")
    question.append(addquestion)
    addans=int(input("give option 1,2,3,4"))
    answer.append(addans)
else:
    for i in question and answer :
        print(question[i-1])
        x=int(input("choose the correct option 1<2<3<4"))
        if i==x:
            print("you won")
            print("congratulations you won")
            print(pricelist[i])
        else:
            print("congratulations total amount of money won by you",pricelist[i]) 
            print("thank you for playing")
            break

