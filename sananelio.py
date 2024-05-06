def nelio(sana, koko):
    a = 0
    l = koko
    for i in range(koko):
        rivi = sana*10
        print(rivi[a:l])
        a+=koko
        l+=koko

nelio("ab", 3)
print()
nelio("aybabtu", 5)