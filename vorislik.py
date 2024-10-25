class Shaxs:
    """Shaxslar Haqida Ma'lumot"""

    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs xaqida ma'lumot"""
        info = f"{self.ism} {self.familiya}, "
        info += f"Passport seriyasi: {self.passport}, {self.tyil}-yilda tug'ilgan"
        return info

    def get_age(self, yil):
        return yil - self.tyil

class Professor(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, fakultet):
        super().__init__(ism, familiya, passport, tyil)
        self.fakultet = fakultet

    def get_info(self):
        info = super().get_info()
        info += f", Fakultet: {self.fakultet}"
        return info

class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, email):
        super().__init__(ism, familiya, passport, tyil)
        self.email = email

    def get_info(self):
        info = super().get_info()
        info += f", Email: {self.email}"
        return info

class Sotuvchi(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, mahsulotlar):
        super().__init__(ism, familiya, passport, tyil)
        self.mahsulotlar = mahsulotlar

    def get_info(self):
        info = super().get_info()
        info += f", Mahsulotlar: {', '.join(self.mahsulotlar)}"
        return info

class Mijoz(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, xaridlar):
        super().__init__(ism, familiya, passport, tyil)
        self.xaridlar = xaridlar

    def get_info(self):
        info = super().get_info()
        info += f", Xaridlar: {', '.join(self.xaridlar)}"
        return info

class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, passport, tyil, email):
        super().__init__(ism, familiya, passport, tyil, email)

    def ban_user(self):
        print("Foydalanuvchi bloklandi.")

professor = Professor("Ali", "Valiyev", "AA1234567", 1998, "Informatika")
foydalanuvchi = Foydalanuvchi("Aliya", "Valiyeva", "AA2345678", 1999, "aliya@gmail.com")
sotuvchi = Sotuvchi("Vali", "Aliyev", "AB3456789", 2000, ["kitob", "qalam"])
mijoz = Mijoz("Valiya", "Aliyeva", "AA4567890", 2001, ["kitob", "qog'oz"])
admin = Admin("Asilbek", "Boyjanov", "AB9876543", 1995, "boyjanov@example.com")

print(professor.get_info())
print(foydalanuvchi.get_info())
print(sotuvchi.get_info())
print(mijoz.get_info())
print(admin.get_info())
admin.ban_user()
