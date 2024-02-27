x=int(input("enter a number which you have to check is prime or not"))
for i in range(2,x):
    if x%i==0:
        print(f"{x} is a not prime number")
        break
else:
    print(f"{x} is a prime number")

#for all the prime number in a given range

