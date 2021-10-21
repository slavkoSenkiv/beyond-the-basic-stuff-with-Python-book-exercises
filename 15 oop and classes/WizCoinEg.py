import wizcoin

purse = wizcoin.WizCoin(2, 5, 99)
print(purse)
print('G:', purse.galleons, 'S:', purse.sickles, 'K:', purse.knuts)
print('total in knuts', purse.to_knuts())
print('weight', purse.weightInGrams(), 'grams')

print()

coinJar = wizcoin.WizCoin(13, 0, 0)
print(coinJar)
print('G:', coinJar.galleons, 'S:', coinJar.sickles, 'K:', coinJar.knuts)
print('total in knuts', coinJar.to_knuts())
print('weight', coinJar.weightInGrams(), 'grams')

print()

change = wizcoin.WizCoin(9, 7, 20)
print('change.sickles', change.sickles)
change.sickles += 10
print('change.sickles+10', change.sickles)

pile = wizcoin.WizCoin(2, 3, 31)
print('pile.sickles', pile.sickles)
pile.someNewAttr = 'a new attr'
print('pile.someNewAttr ', pile.someNewAttr )
