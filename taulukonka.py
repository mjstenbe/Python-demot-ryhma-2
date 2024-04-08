import statistics

taulu = [4, 12,5,13,5,0,6,5,9,0]

print( sum( taulu ) )
print ( statistics.mean( taulu ) )

i = 0
summa = 0
while i < len(taulu):
    summa += taulu[i]
    i+=1
print("Summa: ", summa)
print("Keskiarvo: ", summa / len(taulu))