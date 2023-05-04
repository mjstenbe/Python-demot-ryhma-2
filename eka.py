def tulostaAakkoset():
    aakkoset = "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ"
    for k in aakkoset:
        print(k, end=' ')

    print()

    i = 65
    while i < 123:
        print(chr(i))
        i += 1

    for k in range(65, 123):
        print(chr(k))


def tulostaNumerot():
    print("1234567890")

    for i in range(1, 11):
        print(i)


# tulostaAakkoset()
tulostaNumerot()
# tulostaAakkoset()
