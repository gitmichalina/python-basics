class Currency_Code_Before:
    def __init__(self, units, cents):
        self.units = units
        self.cents = cents

    # Currency implementation...


# currency.py

CENTS_PER_UNIT = 100


class Currency_Code_After:
    def __init__(self, units, cents):
        self._total_cents = units * CENTS_PER_UNIT + cents

    @property
    def units(self):
        return self._total_cents // CENTS_PER_UNIT

    @units.setter
    def units(self, value):
        self._total_cents = self.cents + value * CENTS_PER_UNIT

    @property
    def cents(self):
        return self._total_cents % CENTS_PER_UNIT

    @cents.setter
    def cents(self, value):
        self._total_cents = self.units * CENTS_PER_UNIT + value

    # Currency implementation...
