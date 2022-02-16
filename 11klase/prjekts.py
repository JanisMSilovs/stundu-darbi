import requests
import string
import math

class Banka:
    def __init__(self, vards, konts, summa):
        self.vards = vards
        self.konts = konts
        self.summa = summa
    
    def izveide(self):

    def sasveicinaties(self):
        print(f'Sveiki! Mani sauc {self.vards}.')

    def kontaatlikums(self):
        print(f'Sveiki! Jūsu konta atlikums ir {self.summa}')

    def papildinat(self, summa, apjoms):
        apjoms = int(input("Labdien! Lūdzu ievadiet cik daudz naudas vēlaties papildināt!:"))
        papildinats = self.summa + apjoms

    def iznemsana(self, naudin):
        naudin = int(input("Labdien! Lūdzu ievadiet cik daudz naudas vēlaties izņemt!:"))
        self.summa = self.summa - naudin
        print(f'Paldies! Jūsu kontā vēl ir {self.summa} ')

eur = Banka("Jānis", "euro", 100)
eur.sasveicinaties()
eur.kontaatlikums()
eur.iznemsana()
eur.kontaatlikums()
eur.papildinat(10, 10)
eur.kontaatlikums()