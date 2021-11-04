import wiz_coin_for_composition as wizcoin


def print_purse(purse):
    print(f'{purse.purse_name}\n'
          f'G:{purse.galleons} S:{purse.sickles} K:{purse.knuts}\n'
          f'total in knuts {purse.to_knuts()}\n'
          f'weight {purse.weightInGrams()} gr\n\n')


def print_customer(customer):
    print(f'\n{customer.name} has {customer.to_knuts()} knuts worth if money\n'
          f'{customer.name}\'s coins weight {customer.weightInGrams()} grams')


class WizardCustomer(wizcoin.WizCoin):
    def __init__(self, name):
        self.name = name
        super().__init__('a', 0, 0, 0)


purse = wizcoin.WizCoin('purse', 2, 5, 99)
print_purse(purse)

coin_jar = wizcoin.WizCoin('coin_jar', 13, 0, 0)
print_purse(coin_jar)

change = wizcoin.WizCoin('change', 9, 7, 20)
print_purse(change)
print('we are goinf to add 10 sickles ')
change.sickles += 10
print_purse(change)

pile = wizcoin.WizCoin('pile', 2, 3, 31)
print_purse(pile)
pile.some_new_attr = 'a new attr'
print('pile.some_new_attr ', pile.some_new_attr )

wizard = WizardCustomer('Alice')
print_customer(wizard)


