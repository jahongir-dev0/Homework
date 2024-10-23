class User:
    def __init__(self, full_name, username, email, age, location):
        self.full_name = full_name
        self.username = username
        self.email = email
        self.age = age
        self.location = location

    def get_info(self):
        return f"Foydalanuvchi: {self.username}, Ismi: {self.full_name}, Email: {self.email}, Yosh: {self.age}, Joylashuvi: {self.location}"

user1 = User("Ruslon Ozodov", "ruslon07", "ruslon07@gmail.com", 17, "Xorazm")
user2 = User("Aliya Mirzaeva", "aliya_m", "aliya_m@gmail.com", 22, "Toshkent")

print(user1.get_info())
print(user2.get_info())
