# Izveido programmu, kura ļauj izveidot bankas kontu (objekts), 
# kurā var ielikt naudu un izņemt to.

# Piemērs, kā tas varētu izskatīties:
# eur = Banka(100)
# eur.iemaksa(20)
# Konta atlikums: 120
# eur.izmaksa(30):
# Konta atlikums: 90
# eur.atlikums()
# Konta atlikums: 90
#
# marcinas = Banka(50)
# utt.

class Banka:
    def __init__(self, summa):
        self.vards = input("Ievadiet savu vārdu!")
        self.konts = input("Ievadiet savu konta numuru!")
        self.summa = summa
        self.pin = int(input("Ievadiet 4 ciparu pin kodu!"))

    def sasveicinaties(self):
        print(f"Sveiki, {self.vards}!, kā es varu jūs šodien asistēt?")

    def kontaatlikums(self):
        print(f'Jūsu konta atlikums ir {self.summa}.')

    def papildinat(self):
        apjoms = int(input("Lūdzu, ievadiet cik daudz naudas vēlaties papildināt!:"))
        self.summa = self.summa + apjoms
        print(f'Papildinājums pieņemts! Jūsu konta atlikums ir {self.summa} eur.')
        
    def iznemsana(self):
        nauda=int(input("Lūdzu, ievadiet cik daudz naudas vēlaties izņemt!:"))
        self.summa = self.summa-nauda
        if self.summa < 0:
            print(f"Jūs nevarat to izdarīt, mēģiniet ar mazāku summu!")
        else:
            print(f'Paldies! Jūsu kontā vēl ir {self.summa} eur.')
    
    def atvadas(self):
        print('''
        ********************************************
        PALDIES PAR TO, KA IZVĒLATIES MŪSU SERVISU!
        ********************************************
        ''')

eur = Banka(100)
eur.sasveicinaties()
eur.kontaatlikums()
eur.iznemsana()
eur.papildinat()
eur.atvadas()

