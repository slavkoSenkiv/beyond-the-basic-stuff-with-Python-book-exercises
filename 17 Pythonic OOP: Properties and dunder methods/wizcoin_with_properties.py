# 1 sickle = 29 knuts
# 1 galleon = 17 sickles | 493 knuts

class WizCoinException(Exception):
    """The wizcoin module raises this when the module is misused"""
    pass


class WizCoin():
    def __init__(self, galleons, sickles, knuts):
        # Create a new WizCoin object with galleons, sickles, and knuts.
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        # NOTE: __init__() methods NEVER have a return statement.

    def to_knuts(self):
        # The value (in knuts) of all the coins in this WizCoin object.
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    def weight_in_grams(self):
        # Returns the weight of the coins in grams.
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)

    @property
    def galleons(self):
        # Returns the number of galleon coins in this object
        return self._galleons

    @galleons.setter
    def galleons(self, value):
        if not isinstance(value, int):
            raise WizCoinException('galleons attr must be set to an int, not a' + value.__class__.__qualname__)
        if value < 0:
            raise WizCoinException('galleons attr must be a positive int, not' + value.__class__.__qualname__)
        self._galleons = value

