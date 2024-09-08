class User:
    def __init__(self, first_name, last_name, age, gender, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = login_attempts

    def describe_user(self):
        # Print user information
        print(f"The Username is {self.first_name} {self.last_name},\nwith age being {self.age} and gender being {self.gender}. ")

    def greet_user(self):
        # Greet the user
        print(f"Hello {self.first_name}")

    def increment_login_attempts(self):
        # Increment login attempts
        self.login_attempts = 1 + self.login_attempts
        print(self.login_attempts)

    def reset_login_attempts(self):
        # Reset login attempts
        self.login_attempts = 0
        print(self.login_attempts)


kp = User("suman", "Malviya", 19, "Male", 15)
akashay = User("Akshay", "Kumar", 52, "Male", 10)
anjali = User("Anjali", 'Malviya', 56, 'Female', 20)

anjali.greet_user()
anjali.describe_user()
akashay.greet_user()
akashay.describe_user()
anjali.increment_login_attempts()
anjali.reset_login_attempts()


class Admin(User):
    def __init__(self, first_name, last_name, age, gender, login_attempts):
        super().__init__(first_name, last_name, age, gender, login_attempts)
        self.privileges = "can add post, can delete post, can ban user!"

    def show_privileges(self):
        # Show admin privileges
        print(f"{self.first_name} can {self.privileges}")


ibhav = Admin("Ibhav", "Malviya", 19, "Male", 5)
ibhav.show_privileges()