class user():
    def __init__(self,user_name,user_class,user_roll_no,user_id):
        self.user_name=user_name
        self.user_class=user_class
        self.user_roll_no=user_roll_no
        self.user_id=user_id
    def describe_user(self):
        print(f' {self.user_id}\n The name is {self.user_name} \n The class of the user is {self.user_class}\n The roll number is {self.user_roll_no}\n ')
    def greet_user(self):
        print(f" Welcome {self.user_id},{self.user_name}")
user1=user('anand',123,23123,1)
user2=user('anyone',456,24546,2)
user3=user('hero',673,67853,3)
user4=user('anyone',467,27897,4)
user1.greet_user()
user1.describe_user()
user2.greet_user()
user2.describe_user()
user3.greet_user()
user3.describe_user()
user4.greet_user()
user4.describe_user()
