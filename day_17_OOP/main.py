class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("Dasha", 7)
user_2 = User("Ivan", 12)
user_2.follow(user_1)

print(user_2.following, user_1.followers)
