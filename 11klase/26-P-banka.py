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
import random
import sys
from tracemalloc import stop
class Banka:
    def __init__(self, summa):
        self.vards = input("Ievadiet savu vārdu!")
        self.konts = input("Ievadiet savu konta numuru!")
        self.summa = summa

    def sasveicinaties(self):
        print(f"""
          ******************************************
              Sveicināts, {self.vards}! 
          ******************************************
          """)

    def kontaatlikums(self):
        ()

    def papildinat(self):
        apjoms = int(input("Lūdzu, ievadiet cik daudz naudas vēlaties papildināt!:"))
        self.summa = self.summa + apjoms
        print()
        
    def iznemsana(self):
        nauda=int(input("Lūdzu, ievadiet cik daudz naudas vēlaties izņemt!:"))
        self.summa = self.summa-nauda
        print()

    def izvele(self):
        print("""
        IZVĒLNE
        1. Konta atlikums
        2. Papildināšana
        3. Izņemšana
        4. Beigšana
        """)
        while True:
            try:
                izvele = int(input("Izvēlaties vienu no opcijām!"))
            except:
                print("Error: Jūs varat izvēlēties tikai no 1, 2, 3, 4")
                continue
            else:
                if izvele == 1:
                    self.kontaatlikums()
                    print(f"""
          ******************************************
             Jūsu kontā pieejamais atlikums:
                       {self.summa}
          ******************************************
          """)
                elif izvele == 2:
                    self.papildinat()
                    print(f"""
          ******************************************
              Papildināšana veiksmīgi izpildīta!                         
              Čeka numurs: {random.randint(10000, 1000000)} 
              Konta īpašnieks: {self.vards}                  
              Konta numurs: {self.konts}                
              Pieejamais atlikums: {self.summa}
              Paldies, ka izvēlējāties tieši mūsu banku!    
          ******************************************
          """)
                elif izvele == 3:
                    self.iznemsana()
                    print(f"""
          ******************************************
              Izņemšana veiksmīgi izpildīta!                         
              Čeka numurs: {random.randint(10000, 1000000)} 
              Konta īpašnieks: {self.vards}                  
              Konta numurs: {self.konts}                
              Pieejamais atlikums: {self.summa}
              Paldies, ka izvēlējāties tieši mūsu banku!    
          ******************************************
          """)
                elif izvele == 4:
                    print(f"""
          ******************************************
              Darbības veiksmīgi izpildītas!                         
              Čeka numurs: {random.randint(10000, 1000000)} 
              Konta īpašnieks: {self.vards}                  
              Konta numurs: {self.konts}                
              Pieejamais atlikums: {self.summa}
              Paldies, ka izvēlējāties tieši mūsu banku!    
          ******************************************
          """)
            break
    
eur = Banka(100)
eur.sasveicinaties
eur.izvele()