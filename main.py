class User:

    def __init__(self, user_id, username):
        print("new user being created...")
        self.id = user_id
        self.username = username
        self.followers=0


user_1 = User("001","Vijit")
print(user_1.followers)

user_2 = User("002","Nim")


print(user_2.username)
