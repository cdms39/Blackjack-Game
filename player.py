class Player():

    def __init__(self):
        self.hand = []
        self.hand_sum = 0

    def add_card(self, card):
        self.hand.append(card)