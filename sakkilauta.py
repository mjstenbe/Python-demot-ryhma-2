def sakkilauta(koko):

    # Tulostetaan tarvittava määrä rivejä
    for j in range(koko):
        tulostaRivi(koko)


def tulostaRivi(koko):
     # Tulostetaan yhden rivin sisältö
        for i in range(koko):
            
            if (i+j) %2 == 0:
                print("1", end='')
            else:
                print("0", end='')
            if i == koko-1:
                print()
      
sakkilauta(3)
sakkilauta(6)