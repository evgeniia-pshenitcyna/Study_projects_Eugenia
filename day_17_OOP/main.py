class User:

    def __init__(self, user_name, user_age):
        self.name = user_name
        self.age = user_age


user_1 = User("Dasha", 7)
print(user_1.name, user_1.age)
