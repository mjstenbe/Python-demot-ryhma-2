taulu = [4, 12,5,13,5,0,-1,5,-99,0]
suurin = taulu[0]
pienin = taulu[0]

print ( min( taulu ) )
print( max( taulu) )
print ( sorted ( taulu ) )

for x in taulu:
    if suurin < x:
        suurin = x
    if pienin > x:
        pienin = x    
print("Suurin oli: ", suurin)
print("Pienin  oli: ", pienin)


    
"""
i = 0

while i < len( taulu ):
    print(x)
    i+=1

while True:
    print( taulu[i] )
    i+=1
    if i == len(taulu)-1:
        break

        suurin = x
"""
