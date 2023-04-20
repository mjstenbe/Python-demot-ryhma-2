fruits = ["apple", "banana", "cherry", "mandarin", "coconut", "pineapple"]
numerot = [0, 12, 23, 23, 43, 324, 563, 234]

pituus = len(fruits)
print(pituus)

for a in fruits:
    print(a)


i = 0
while True:
    print(fruits[i])
    i += 1
    if (i == pituus-1):
        break

i = 0
while i < pituus:
    print(fruits[i])
    i += 1

j = 0
while j < 7:
    print(numerot[j])
    j += 1
