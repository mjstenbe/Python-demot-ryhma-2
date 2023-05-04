def meiliKyselija():
    meili = input("Syötä sähköpostiosoite: ")

    if meili.find('@') > 0 and len(meili) > 6:
        print("Oli kelvollinen sähköpostiosoite.")

        return True
    else:
        print("Ei ole kelvollinen sähköpostiosoite.")
        return False


while True:
    if meiliKyselija():
        break
