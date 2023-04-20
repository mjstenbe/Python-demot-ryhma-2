# Tämä viimeistä esimerkkiä varten
from statistics import mean

i = 0
taulukko = []
summa = 0

while i < 5:
    arvosana = int(input("Syötä arvosana "+str(i)+": "))
    summa += arvosana
    taulukko.append(arvosana)
    i += 1
# Tulostetaan taulukko silmukan ulkopuolella

print(taulukko)
print("Lukujen summa on: " + str(summa))
print(f"Lukujen keskiarvo on: {sum(taulukko) / len(taulukko)}")

# Voidaan käyttää myös valmiita funktioita statistics-kirjastosta
print(f"Lukujen keskiarvo on: {mean(taulukko)}")
print(f"Lukujen keskiarvo on: {summa / len(taulukko)}")
