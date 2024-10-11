def ism_sora(yil, xozir=2024):
    """Foydalanuvchi Yoshini Aniqlaydigan Dastur"""
    if yil == xozir:
        print("Siz hali Tug'ilmagansiz")
    else:
        print(f"Siz {xozir - yil} yoshdasiz")
ism_sora(2024)

# Keyingi ->

def yil_sora(son):
    """Sonning Kvadratini Aniqlaydigan Funksiya"""
    print(f"Sonning Kvadrati: {son**2}, Sonning Kubi: {son**3}")
yil_sora(10)

# Keyingi ->

def juft_toq(raqam):
    """JufYoki Toq sonni Aniqlaydigan Funksiya"""
    if raqam%2 == 0:
        print("Bu Raqam Juft Son")
    else:
        print("Bu Toq Son")
juft_toq(20)