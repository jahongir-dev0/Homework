def hisobla(*sonlar):
    natija = 1
    """Sonlarni Ko'paytmasini Hisoblab Beruvchi Funkisya"""

    for son in sonlar:
        natija *= son
    return natija
print(hisobla(2,5,2))

#Keyingi ->
def kvadrat_his(majbur1, majbur2, majbur3, *sonlar):
    natijalar = [majbur1**2, majbur2**2, majbur3**2]
    for son in sonlar:
        natijalar.append(son**2)
    return natijalar

print(kvadrat_his(2,5,8))
print(kvadrat_his(1,2,3,4, 5, 6))

#Keyingi ->
def talaba_mal(ism, familiya, **malumotlar):
    talaba = {
        'ism': ism,
        'familiya': familiya
    }

    for kalit, qiymat in malumotlar.items():
        talaba[kalit] = qiymat
    return talaba

talaba1 = talaba_mal('Ali', 'Valiyev', yosh=20, kurs=3, faklutet='Kiber havfsizlik')
talaba2 = talaba_mal('Aliya', 'Valiyeva', yosh=19, kurs=2, faklutet='Logistika')

print(talaba1)
print(talaba2)