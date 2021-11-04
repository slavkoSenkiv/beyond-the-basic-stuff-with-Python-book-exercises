
# 1 sickle = 29 knuts
# 1 galleon = 17 sickles | 493 knuts

class WizCoin():
    def __init__(self, purse_name, galleons, sickles, knuts):
        # Create a new WizCoin object with galleons, sickles, and knuts.
        self.purse_name = purse_name
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        # NOTE: __init__() methods NEVER have a return statement.

    def to_knuts(self):
        # The value (in knuts) of all the coins in this WizCoin object.
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    def weightInGrams(self):
        # Returns the weight of the coins in grams.
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)


