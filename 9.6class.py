"""9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method."""
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
class IceCreamStand(restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavor=['mango','pineapple','chocolate','butterschoces','no flavor']
    def flavors(self):
        print(self.flavor)
icecram=IceCreamStand('anand','indian')
icecram.flavors()
icecram.describe_restaurant()
