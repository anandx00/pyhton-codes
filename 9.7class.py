"""9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method."""
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
class privilege():
    def __init__(self):
        self.privileges=["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(self.privileges)
class admin(user):
    def __init__(self,user_name,user_class,user_roll_no,user_id):
        super().__init__(user_name,user_class,user_roll_no,user_id)
        self.privileges=privilege()



admin_1=admin('anand',688,456789,788888)
admin_1.privileges.show_privileges()

print(admin_1.user_name)