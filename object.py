class Avto:
    def __init__(self, model, rang, narh, yil, km=0):
        self.model = model
        self.rang = rang
        self.narh = narh
        self.yil = yil
        self.km = km

    def get_info(self):
        """Avto haqida ma'lumot beruvchi metod"""
        return f"Model: {self.model}, Rang: {self.rang}, Narh: {self.narh}$, Yili: {self.yil}, Yurgan: {self.km} km"

    def update_km(self, km):
        """Kilometrajni yangilovchi metod"""
        if km >= self.km:
            self.km = km
        else:
            print("Xatolik: kmni kichik qiymatga o'zgartirish mumkin emas.")

class Avtosalon:
    """Avtosalon klassi"""
    def __init__(self, nomi, manzil):
        self.nomi = nomi
        self.manzil = manzil
        self.avtomobillar = []

    def add_avto(self, avto):
        """Salonga yangi avtomobil qo'shish metodi"""
        self.avtomobillar.append(avto)

    def get_avtomobillar(self):
        """Salondagi barcha avtomobillar haqida ma'lumot beruvchi metod"""
        for avto in self.avtomobillar:
            print(avto.get_info())

# Obyektlar yaratish
avto1 = Avto("BMW M5 CS", "Oq", 145000, 2021)
avto2 = Avto("BMW M4 Competition", "Qora", 89000, 2025)

salon = Avtosalon("AvtoMarket", "Toshkent")

# Avtomobillarni salonga qo'shish
salon.add_avto(avto1)
salon.add_avto(avto2)

# Salondagi barcha avtomobillar haqida ma'lumot chiqarish
salon.get_avtomobillar()

# KMni yangilash
avto1.update_km(20000)
print("\nYangilangan ma'lumot:")
print(avto1.get_info())