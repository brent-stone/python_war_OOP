from Deck import Deck
from collections import OrderedDict


class Player:
    def __init__(self):
        self.draw_pile = Deck()
        self.discard_pile = Deck()
        self.record = OrderedDict()

    def take_card(self, card: tuple):
        self.discard_pile.add_card(card)

    def take_cards(self, cards: list):
        self.discard_pile.add_cards(cards)

    def shuffle(self):
        self.draw_pile.pile += self.discard_pile.pile
        self.discard_pile.empty_pile()
        self.draw_pile.shuffle()

    def shuffle_check(self, n: int):
        if self.draw_pile.count() <= n:
            self.shuffle()

    def play_card(self):
        self.shuffle_check(1)
        return self.draw_pile.draw()

    def play_war(self, n: int):
        self.shuffle_check(n)
        return self.draw_pile.draw_n(n)

    def score(self):
        return self.draw_pile.count() + self.discard_pile.count()

    def update_record(self, turn: int):
        self.record[turn] = self.score()
