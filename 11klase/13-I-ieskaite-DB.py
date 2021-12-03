###
# Programma "Muzejs" aprēķina par ieeju maksājamo summu muzejā,
# atkarībā no pieaugušo un skolēnu skaita, kā ari to, vai pienākas bezmaksas apmeklējums
#
# Atkarībā no pieaugušo un skolēnu skaita, cena tiek noteikta šādi:
# Vienas pieaugušo biļetes cena ir 8 EUR
# Vienas skolēnu biļetes cena ir 2.5 EUR
# Ja muzeju apmeklē 1 pieaugušais un 2 līdz 4 skolēni, piemēro ģimenes biļetes cenu 12 EUR
# Ja muzeju apmeklē 2 pieaugušie un 2 līdz 4 skolēni, piemēro ģimenes biļetes cenu 16 EUR
# Ja grupā ir 10 un vairāk skolēni, viņiem biļete maksā 1 EUR katram
#
#
# DB jāieraksta visi ievades dati un aprēķinātā summa
#
# Jāizveido vaicājums, kurš parāda tikai bezmaksas apmeklējumus
# Es nesaprotu kāpēc man neļauj ielikt vērtības iekšā tabulā. Mēģināju visu, ko vien varēju, tāpat neiet. gan summa, gan ? 3x, es nezinu ko darīt.
# Jautājums. Kādu vēl tabulu varētu pievienot šajā DB – kādi datu lauku tajā būtu?
# Varētu pievienot 'akcijas', kur būtu skolēnu, ģimenes akcijas ar summu, ko zaudē, kad tiek pielietota akcija. Piemēram, lauks - parastā cena 10eur, akcija - 5eur,
#apkalpošana 4eur, peļņa - 1 eur. Arī lauks ID kā integrer un automātiski palielinās
# Kurš no tiem varētu būt kopīgs ar šo Tevis izveidoto tabulu, ja tā tiktu papildināta?
### Varētu šo pašu arī pielikt klāt šim, bet tas būtu ļoti, ļoti piņķerīgi. Te arī ir par akcijām, tikai daudz vienkāršāk.
import sqlite3
conn = sqlite3.connect('lv_filmas.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS lv_filmas(cenaPieaugusie REAL, skoleni REAL, pieaugusie REAL, ID INTEGER PRIMARY KEY AUTOINCREMENT)')

def muzejs():
    cenaPieaugusie = 8
    cenaSkoleni = 2.5
    gimenes = False

    pieaugusie = int(input("Cik pieaugušie apmeklētāji?"))
    skoleni = int(input("Cik skolēni?"))
    vaiBezmaksas = input("Vai pienākas bezmaksas apmeklējums? j/n")

    if vaiBezmaksas == "j":
        bezmaksas = True
    else:
        bezmaksas = False
    
    if bezmaksas:
        summa = 0
    elif pieaugusie == 1 and 2<=skoleni<=4:
        summa = 12
        gimenes = True
    elif pieaugusie == 2 and 2<=skoleni<=4:
        summa = 16
        gimenes = True
    elif skoleni>=10:
        summa = skoleni + cenaPieaugusie*pieaugusie
    else:
        summa = cenaSkoleni*skoleni + cenaPieaugusie*pieaugusie
    
    print(summa)

cur.execute('INSERT INTO lv_filmas( cenaPieaugusie, skoleni, pieaugusie ) VALUES ()')
#Kaut kas ļoti nesanāk, nesaprotu, kur ir mana kļūda.

def beigas():
    cur.cloce()
    conn.close()





cur.execute('SELECT bezmaksas FROM muzejs')
    
