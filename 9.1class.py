class restaurant():
    def __init__(self ,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print("the resturant name is ",self.restaurant_name.title())
        print("the cuisine type is ",self.cuisine_type.title())
    def open_restaurant(self):
        print('restaurant opens at 10 am and closes at 10 pm')
restaurant1=restaurant('anand restaurant','indian')
restaurant2=restaurant('idk','pakistani')
restaurant3=restaurant('hello','swidish')
print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)
restaurant1.describe_restaurant()
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
