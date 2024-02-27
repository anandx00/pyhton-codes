class employ:
    def __init__(self,name ,clas,rollno,passcode):
        self.name=name
        self.clas=clas
        self.rollno=rollno
        self.passcode=passcode
        self.gmail=name+clas+rollno+passcode+'@gmail.com'
    def fullname(self):
        return f'{self.name}{self.clas}'
    

emp1=employ('anand','andn','andnf','andnafsd')
print(emp1.gmail)
print(emp1.fullname())
print(employ.fullname(emp1))# another method for same thing

class bossemploy(employ):
    def __init__(self,extra,*args,**kwargs):#  *args , kwargs means copy all the thing from the first 
        self.extra=extra
        super().__init__(*args,**kwargs)
emp2=bossemploy('kumar','anand','andn','andnf','andnafsd')
print(bossemploy.name(emp2))
