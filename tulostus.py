nimi = "Mika"
pituus = 178.3333333333333

# Normitulostus
print("Hoi Maailma!")
print("Terve " + nimi)
print("Terve %s olet %.2f pitkä." % (nimi, pituus))

# f-muotoiltu tulostus
print(f"Terve {nimi} olet {pituus:.2f} pitkä.")

# Tulostus ilman rivinvaihtoa
print("Hello there! ", end='')
print("It is a great day.")
