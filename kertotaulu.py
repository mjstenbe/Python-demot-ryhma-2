luku = int(input("Anna luku: "))
i = 1
while i <= 20:
    print(f"{i:<+10.2f} x {luku:^4d} = {i*luku}")
    # print( i, " x ", luku, " = ", i*luku)
    # print(str(i) + " x " + str(luku) + " = " + str(i*luku))
    i+=1