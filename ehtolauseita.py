tilinSaldo = 5
kauppaOnAuki = False

if tilinSaldo == 0:
    if kauppaOnAuki == False:
        print("Huono flaksi.")


if tilinSaldo == 0 or kauppaOnAuki == False:
    print("Huono flaksi.")

if tilinSaldo > 0 and kauppaOnAuki == True and 10 < 20:
    print("Tilaa pitsa.")
    print("Katso leffa.")

else:
    print("Mene lenkille")
    print("Käy suihkussa")
