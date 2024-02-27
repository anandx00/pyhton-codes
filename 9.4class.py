"""9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any num-
ber you like that could represent how many customers were served in, say, a
day of business."""
class restaurant():
    def __init__(self ,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print("the resturant name is ",self.restaurant_name.title())
        print("the cuisine type is ",self.cuisine_type.title())
    def open_restaurant(self):
        print('restaurant opens at 10 am and closes at 10 pm')
    def set_number_served(self,no_coustomer):
        self.number_served=no_coustomer
    def increment_number_served(self):
        self.number_served+=1
restaurant1=restaurant('andaf','indian')
print(restaurant1.number_served)
restaurant1.number_served=4
print(restaurant1.number_served)
restaurant1.set_number_served(7)
print(restaurant1.number_served)
restaurant1.increment_number_served()
print(restaurant1.number_served)



