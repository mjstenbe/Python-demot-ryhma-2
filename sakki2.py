def sakkilauta(koko):
    #  Tulosta n kpl rivejä
    for j in range(koko):
        print()
        # Tulosta koko kappaletta merkkejä riviä kohden
        for i in range(koko):
            if (i+j) % 2 == 0:
                print("1", end='')
            else:
                print("0", end='')

sakkilauta(5)
print()
sakkilauta(10)
print()
sakkilauta(3)