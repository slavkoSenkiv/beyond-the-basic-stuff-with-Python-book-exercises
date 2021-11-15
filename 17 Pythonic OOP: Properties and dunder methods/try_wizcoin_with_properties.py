import wizcoin_with_properties as wizcoin

purse = wizcoin.WizCoin(5, 15, 25)

print(purse.galleons)
print(purse.sickles)
print(purse.knuts)

print(purse.to_knuts())
print(purse.weight_in_grams())

purse.galleons = 1
print(purse.galleons)
purse.galleons = -1
print(purse.galleons)
