# table calculator
x=int(input("enter a number to print table of a number"))
for i in range(1,11):
   y=i*x
   print(f"{x} x {i} == {y}")


#to reverse anything

#x=input("enter a word which you have to reverse it")
#k=[]
#for i in x:
#    k.append(i)
#print(k)
#k.reverse()
#print(k)
#''.join(k)palimdrome.py


#to find wheather a number is palindrome or not
x=input("enter a string")
k=list(map(lambda q:q ,x))
print(k)
i=k.copy()
k.reverse()
y=k.copy()
if (i==y):
    print("palindrome")
else:
    print ("not a palindrome")
if x==x[::-1]:
    print("palindrome")
else:
    print ("not a palindrome")