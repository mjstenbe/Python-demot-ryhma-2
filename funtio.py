def summa(ekaluku, tokaluku):
    tulos = ekaluku+tokaluku
    print(tulos)
    return tulos


def erotus(ekaluku, tokaluku):
    tulos = ekaluku-tokaluku
    return tulos


erotus(456, 567)


komento = input("Anna komento: ")
if komento == "summa":
    summa(34, 45)
elif komento == "erotus":
    erotus(344, 243)
else:
    print("En ymmärrä komentoa.")


def viesti():
    print("Tämä on oma funktio!")


def toinenviesti(viesti):
    print("******************************")
    print("****** " + viesti + " *********")
    print("******************************")


# Funktiota kutsutaan nimellä
viesti()

toinenviesti("Hoi Maailma")
toinenviesti("Python ohjelmointi on mukavaa")
toinenviesti("Ohjelman valikko")

a = summa(23, 50)
b = summa(4, 12)
c = summa(a, b)

print(summa(234, 2456))

print("Muuttujan a arvo on " + str(a))
print("Muuttujan a arvo on " + str(b))
print("Muuttujan a arvo on " + str(c))
