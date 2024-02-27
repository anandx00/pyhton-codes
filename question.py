
a=input("enter any value less than  5 and more than 9  or an quit")
try:
    if (int(a))>5 or (int(a))<9:
      raise ValueError
except ValueError:
    print()
if a=='quit':
        print("no error")
else:
    raise ValueError


