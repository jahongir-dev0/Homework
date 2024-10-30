class Shaxs:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Yosh manfiy bo'lishi mumkin emas.")

class Account:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} mablag' qo'shildi.")
        else:
            print("Miqdor musbat bo'lishi kerak.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} mablag' yechildi.")
        else:
            print("Yaroqsiz miqdor.")

    def get_balance(self):
        return "Balansni ko'rish mumkin emas."

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary, manager=False):
        if manager:
            self.__salary = salary
            print("Maosh yangilandi.")
        else:
            print("Faqat menejer maoshni yangilashi mumkin.")
