mes = {
    "klase": "11.a",
    "audzinātāja": "Aija",
    "skaits": 22,
    "kabinets": "304",
    "skoleni": {
        "1": "Rihards",
        "2": "Simona",
        "3": "Aleksis",
        "4": "Dāvis",
        "5": "Keita",
        "6": "Madara",
        "7": "Madara",
        "8": "Domeniks",
        "9": "Diāna",
        "10": "Edgars",
        "11": "Laura",
        "12": "Verners",
        "13": "Katrīna",
        "14": "Emīls",
        "15": "Signe",
        "16": "Anita",
        "17": "Baiba",
        "18": "Linards",
        "19": "Jānis",
        "20": "Nikola",
        "21": "Luīze",
        "22": "Klinta"
    },
    "priekšmeti" : [
        "Angļu valoda", "Bioloģija", "Fizika", "Ģeogrāfija", "Klases stunda", "Krievu valoda", "Kultūras pamati", "Ķīmija", "Latviešu valoda", "Literatūra", "Matemātika", "Programmēšana", "Sociālās zinības un vēsture", "Sports un veselība", "Vācu valoda", "Koris", "Teātris"
    ]
}

# Visas atslēgas no vārdnīcas


# Visas vērtības no vārdnīcas

# SELECT * FROM mes

# Tikai atslēgas "skoleni" vērtības

# SELECT skoleni FROM mes

# Tikai savu vārdu

#SELECT * FROM skoleni WHERE ID like '19'

# Tikai atslēgas "priekšmeti" vērtības stabiņā uz leju

#SELECT priekšmeti FROM mes ORDER BY DESC