class User:
    def __init__(self, full_name, username, email, age, location):
        self.full_name = full_name
        self.username = username
        self.email = email
        self.age = age
        self.location = location

    def get_info(self):
        return f"Foydalanuvchi: {self.username}, ismi: {self.full_name}, email: {self.email}, yosh: {self.age}, joylashuvi: {self.location}"

# Bir nechta foydalanuvchi obyektlarini yaratamiz
user1 = User("Alijon Valiyev", "alijon1994", "alijon1994@gmail.com", 30, "Toshkent")
user2 = User("Aliya Mirzaeva", "aliya_m", "aliya_m@gmail.com", 28, "Samarqand")

# Obyektlarning metodlarini chaqirish
print(user1.get_info())
print(user2.get_info())
