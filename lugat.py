menu = {
    'Somsa': 8000,
    'Mantı': 18000,
    'Lagmon': 27000,
    'Chuchvara': 24000
}

ovqat1 = input("1chi Ovqatni Kiriting: ")
ovqat2 = input("2chi Ovqatni Kiriting: ")
ovqat3 = input("3chi Ovqatni Kiriting: ")

buyurtmalar = [ovqat1, ovqat2, ovqat3]

for ovqat in buyurtmalar:
    if ovqat in menu:
        print(f"{ovqat} Narxi: {menu[ovqat]} sum")
    else:
        print(f"Bizda {ovqat} degan taom yo'q!")

# # 2-chi
kirit = input("Davlat Nomini Kiriting: ")

davlatlar = {
    'Uzbekistan': 'Tashkent',
    'USA': 'Washington D.C',
    'Turkey': 'Istanbul',
    'France': 'Paris',
    'Japan': 'Tokyo',
    'Brasilia': 'Brasilia',
    'Italy': 'Rome',
    'India': 'New Delhi'
}

if kirit in davlatlar:
    print(f"Bu Davlatning Poytaxti: {davlatlar[kirit]}")
else:
    print("Bizda Bunday Ma'lumot Yo'q")

# # 3-chi
python_lugat = {
    "append": "Ro'yxatning oxiriga yangi element qo'shish uchun ishlatiladi.",
    "del": "Obyektni yoki elementni o'chirish uchun foydalaniladi.",
    "upper": "Matndagi barcha harflarni katta harflarga o'zgartiradi.",
    "lower": "Matndagi barcha harflarni kichik harflarga o'zgartiradi.",
    "sorted": "Berilgan ro'yxatni yoki to'plamni tartiblaydi.",
    "len": "Ro'yxatdagi elementlarning uzunligini tashlaydi va qaytaradi.",
    "insert": "Ro'yxatning ma'lum bir joyiga yangi element qo'shadi.",
    "range": "Berilgan oralig'ida ketma-ket sonlar yaratadi.",
    "reverse": "Ro'yxatni teskari tartibda o'zgartiradi."
}

for pyLugat in sorted(python_lugat):
    print(f"{pyLugat.capitalize()}: {python_lugat[pyLugat]}")
