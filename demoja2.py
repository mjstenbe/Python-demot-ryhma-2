taulu = [12, 342, 234, 456, 345]

i = 0
while True:
    # Kun ollaan viimeisen alkion kohdalla
    if i == 4:
        print(taulu[i])
        break
    # Kaikkien muiden alkioiden kohdalla
    else:
        print(taulu[i], end=', ')
    # Kasvatuslause
    i += 1
