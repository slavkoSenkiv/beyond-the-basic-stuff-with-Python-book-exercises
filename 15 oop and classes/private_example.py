class BankAccount:
    def __init__(self, accountHolder):
        # BankAccount methods can access self._balance, but code outside of this class should not:
        self._balance = 0
        self._name = accountHolder
        with open(self._name + 'Ledger.txt', 'w') as ledgerFile:
            ledgerFile.write('Balance is 0\n')

    def deposit(self, amount):
        if amount <= 0:
            return  # don't allow negative deposit
        self._balance += amount
        with open(self._name + 'Ledger.txt', 'a') as ledgerFile:
            ledgerFile.write('Deposit ' + str(amount) + '\n')
            ledgerFile.write('Balance is ' + str(self._balance) + '\n')

    def withdraw(self, amount):
        if self._balance < amount or amount < 0:
            return  # Not enough in account, or withdraw is negative
        self._balance -= amount
        with open(self._name + 'Ledger.txt', 'a') as ledgerFile:
            ledgerFile.write('Withdraw ' + str(amount) + '\n')
            ledgerFile.write('Balance is ' + str(self._balance) + '\n')


acct = BankAccount('Alice')  # We create an account for Alice
acct.deposit(120)  # _balance can be affected through deposit()
acct.withdraw(40)  # _balance can be affected through withdraw()

# Changing _name or balance outside of BankAccount is impolite, but allowed
acct._balance = 1000000000
acct.withdraw(1000)

acct._name = 'Bob'  # Now we are modifying Bobs account ledger!
acct.withdraw(1000)  # this withdrawal is recorded in BobLedger.txt!


