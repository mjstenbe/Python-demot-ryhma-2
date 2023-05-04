
email = input("Anna meiliosoite: ")

if email.find('@') > 0 and len(email) > 6:
    print("On kelvollinen sähköposti")
else:
    print("Ei kelpaa!")

print(email.find('@'))
