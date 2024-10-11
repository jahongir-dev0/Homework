def ism_sora(yil, xozir=2024):
    """Foydalanuvchi Yoshini Aniqlaydigan Dastur"""
    if yil == xozir:
        print("Siz hali Tug'ilmagansiz")
    else:
        print(f"Siz {xozir - yil} yoshdasiz")
ism_sora(2007)

# Keyingi ->

def yil_sora(son):
    """Sonning Kvadratini Aniqlaydigan Funksiya"""
    print(f"Sonning Kvadrati: {son**2}, Sonning Kubi: {son**3}")
yil_sora(10)

# Keyingi ->

def juft_toq(raqam):
    """JufYoki Toq sonni Aniqlaydigan Funksiya"""
    if raqam%2 == 0:
        print("Bu son Juft Son")
    else:
        print("Bu Toq Son")
juft_toq(21)

# Keyingi ->

def katta_teng(number, number2):
    if number > number2:
        print(f"{number} raqami {number2} raqamidan Katta")
    elif number2 > number:
        print(f"{number2} raqami {number} raqamidan Katta")
    else:
        print("Sonlar Teng")
katta_teng(5, 5)