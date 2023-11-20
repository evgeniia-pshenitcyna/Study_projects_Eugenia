class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.followers = 0


user_1 = User("Dasha", 7)
print(f"Name: {user_1.name}, age: {user_1.age}, followers: {user_1.followers}")
