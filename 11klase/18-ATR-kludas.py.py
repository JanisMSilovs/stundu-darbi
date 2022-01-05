#Izveido programmu, kurā met mega lielu, krutu kauliņu. Ja punktu skaits ir mazāks vai vienāds ar 6 (līdz 0), tad esi uzvarējis. Ja punktu skaits ir no 6 līdz 12, tad ir neizšķirts.
#Savukārt, ja punkti svārstās no 12 līdz 16 - tad esi zaudējis. Programmai jāparāda vai uzvarēji, vai neizšķirts, vai zaudēji. Ja skaits ir 0 tad kā tādu dabūji?
#Uz negatīviem skaitļiem programmai jāsaka "Zaudēji", jo viltnieki nevienam nepatīk. Decimālskaitļi programmā nav paredzēti, tikai reāli skaitļi. Ar kauliņu uzmest decimālskaitli nav iespējams.
def punkti():
    skaits = int(input("Ievadi punktu skaitu no 1 līdz 16"))
    if skaits == 0:
        print("Ups! Kā dabūji 0?")
    elif skaits > 0 and skaits <= 6:
        print("Mēs uzvarējām!")
    elif skaits > 6 and skaits < 12:
        print("Neizšķirts!")
    elif skaits <= 12 and skaits <= 16:
        print("Zaudēji!")
    else:
        print("Nav iespējams, notikusi kļūda rēķinot!")

# TESTS
# 1 ; 2 ; 3 ; 4 ; 5 ; 6 - Uzvara.
# 7 ; 8 ; 9 ; 10 ; 11; 12 - Neizšķirts.
# 12 ; 13; 14; 15; 16 - Zaude.
# 17 - neizšķirts
# -17 - Zaudēji!
# 0 - Ups! Kā dabūji 0?
# 2,3 - nav paredzēts, kļūda

