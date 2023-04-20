kokonaislukutaulukko = [5, 7, 32, 31, 8]
dm = [12.4, -13.55, 67.44]
kaupungit = ["Helsinki", "Lissabon", "New York", "Shanghai"]

l = 0
while l < len(kokonaislukutaulukko):
    print(kokonaislukutaulukko[l], end=", ")
    l += 1
print()

print("Alkiossa 3 on: " + kaupungit[2])
print(f"Alkiossa 3 on: {kaupungit[2]}")

print("Taulukossa on " + str(len(kokonaislukutaulukko)) + " alkiota.")

print(f"Taulukossa on {len(kokonaislukutaulukko)}")
