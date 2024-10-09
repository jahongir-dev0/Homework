assarlari = {
    "Abu Abdullah Muhammad ibn Ismoil": [
        "Al-jome` as-sahih",
        "Al-adab al-mufrad",
        "At-tarix al-kabir",
        "At-tarix as-sag'ir"
    ],
    "Abdulla Qodiriy": [
        "O'tkan kunlar",
        "Mehrobdon Chayon",
        "Obid ketmon"
    ],
    "Erkin Vohidov": [
        "Tong nafasi",
        "Go'shig'larim sizga",
        "Ozbegim",
        "G'uzalqucham Matmusa"
    ],
    "Alisher Navoyi": [
        "Xamsa",
        "Lison ut-tayr",
        "Mahbub Al-Qulub",
        "Munojot"
    ]
}

for ism, asarlar in assarlari.items():
    print(f"{ism} ning mashhur asarlari:")
    for asar in asarlar:
        print(f" - {asar}")
    print()

# # 2-chi

do_stlar_filmlari = {
    "Alining sevimli kinolari": [
        "Termanitor",
        "Rambo",
        "Titanic"
    ],
    "Valining sevimli kinolari": [
        "Tenet",
        "Inception",
        "Interstellar"
    ],
    "Hasanning sevimli kinolari": [
        "Abdullajon",
        "Bomba",
        "Shaytanat"
    ],
    "Husanning sevimli kinolari": [
        "Mahallada duv-duv gap",
        "John Wick"
    ]
}

for ism, filmlar in do_stlar_filmlari.items():
    print(f"{ism}: {', '.join(filmlar)}")

# # 3-chi
davlatlar = {
    "O'zbekistonning poytaxti": {
        "Hududi": "4489708 kv.km",
        "Aholisi": 33000000,
        "Pul birligi": "so'm"
    },
    "Rossiyaning poytaxti": {
        "Hududi": "17098246 kv.km",
        "Aholisi": 144000000,
        "Pul birligi": "rub"
    }
}

for davlat, info in davlatlar.items():
    print(f"{davlat} ning poytaxti: {info['poytaxt']}")
    print(f"Hududi: {info['Hududi']}")
    print(f"Aholisi: {info['Aholisi']}")
    print(f"Pul birligi: {info['Pul birligi']}\n")
