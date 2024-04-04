kurssi = 5.94573

print(30*"*")
print("* Euroa      =     Markkaa   *")
print("******************************")


for i in range(1,11):
    print(f"{i:^6} = {i*kurssi:^10.2f}")
