#### Uy Ishi-1

kitoblar = []
ishora = True

while ishora:
    kitob = input("Yaxshi Ko'rgan Kitobingizni kirting: ")
    kitoblar.append(kitob)

    javob = input("Davom Etasizmi? (ha/stop): ").lower()

    if javob == 'stop':
        break

print(f"Siz Yoqtirgan Kitoblar: {', '.join(kitoblar)}")

#### Uy Ishi-2
buyurtmalar = []
ishora = True

while ishora:
    kirit = "Buyurtma Kiriting: "
    buyur = input(kirit)
    buyurtmalar.append(buyur)
    javob = input("Yana Buyurtma Berasizmi? (ha/no): ")

    if javob == 'ha':
        continue
    else:
        break

print(f"Sizning Buyurtmalaringiz: {buyurtmalar}")
