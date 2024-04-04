kokonaislukutaulukko = [5, 7, 32, 31, 8]
dm = [12.4, -13.55, 67.44]
kaupungit = ["Helsinki", "Lissabon", "New York", "Shanghai"]


# Taulukom tulostaminen
i = 0
koko = len(kokonaislukutaulukko)

while i < koko:
     print( kokonaislukutaulukko[i])
     i+=1

# Taulukon tulostaminen käänteisestä

j = len(dm)-1
while j >= 0:
    print( dm[j] )
    j=j-1



l = 0
while l < len(kokonaislukutaulukko):
    if l == len(kokonaislukutaulukko)-1:
        print(kokonaislukutaulukko[l])    
    else: 
        print(kokonaislukutaulukko[l], end=", ")
    l += 1
print()




print("Alkiossa 3 on: ", kaupungit[2])
print("Alkiossa 3 on: " + kaupungit[2])
print(f"Alkiossa 3 on: {kaupungit[2]}")

print("Taulukossa on " + str(len(kokonaislukutaulukko)) + " alkiota.")
print("Taulukossa on ", len(kokonaislukutaulukko), " alkiota.")
print(f"Taulukossa on {len(kokonaislukutaulukko)}")
 