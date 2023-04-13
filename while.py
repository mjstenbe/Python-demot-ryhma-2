

# Eka versio
while pin != 1234:
    pin = int(input("Anna pin-koodi: "))

# Toinen versio
while True:
    pin = int(input("Anna pin-koodi: "))
    if pin == 3210:
        print("Nyt meni oikein!")
        break
