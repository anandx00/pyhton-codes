"""9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0."""
class user():
    def __init__(self,user_name,user_class,user_roll_no,user_id):
        self.user_name=user_name
        self.user_class=user_class
        self.user_roll_no=user_roll_no
        self.user_id=user_id
        self.login_attempts=0
    def describe_user(self):
        print(f' {self.user_id}\n The name is {self.user_name} \n The class of the user is {self.user_class}\n The roll number is {self.user_roll_no}\n ')
    def greet_user(self):
        print(f" Welcome {self.user_id},{self.user_name}")
    def increment_login_attempts(self):
        self.login_attempts +=1
    def reset_login_attempts(self):
        self.login_attempts=0
user1=user('ananf',789,234324,38180234)
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)