class cards():
    def __init__(self, value, number, kind=''):
        self.value = value
        self.number = number
        self.kind = kind

    # Returns the card number

    def card_number(self):
        return self.number

    # Returns the card's value

    def card_value(self):
        return self.value

    # Returns the card's name

    def card_kind(self):
        return self.kind
