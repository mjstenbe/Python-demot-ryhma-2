def nelio(sana, koko):
    # Indeksien alku ja loppu
    a = 0
    l = koko
    # Tulostetaan rivejä koko kertaa
    for i in range(koko):
        rivi = sana*10
        # Tulostetaan rivi indeksien a ja l väliltä
        print(rivi[a:l])
        # Kasvatetaan indeksien paikkaa sanan pituuden verran
        a+=koko
        l+=koko

nelio("ab", 3)
print()
nelio("aybabtu", 5)