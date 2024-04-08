rahaa = 100
kauppaOnAuki = True

while rahaa > 0 and kauppaOnAuki == True:
    print("Ostetaan levy.")
    rahaa = rahaa-20
    kauppaOnAuki = False
print("Rahat loppuivat tai kauppa meni kiinni!")