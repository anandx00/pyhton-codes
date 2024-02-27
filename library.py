class library():
    def __init__(self):
        self.books=[]
        self.no_of_books=0
    def addbooks(self,book):
        self.books.append(book)
        self.no_of_books=len(self.books)
    def remove(self,book):
        try:
            self.books.remove(book)
            self.no_of_books=len(self.books)
        except:
            return 'book doesnt exist'
    def showinfo(self):
        print(f'{self.books},{self.no_of_books}')
l=library()
x=int(input('enter a number of books you want to enter = '))
for i in range(x):
    i=l.addbooks(input('enter the name of book  =  '))  
# l.addbooks("anand")
l.showinfo()
l.remove("anand")
l.showinfo()

    
    