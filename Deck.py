from Card import Card
import random


class Deck:
    def __init__(self, full_pile: bool = False):
        self.pile = []
        if full_pile:
            # generate the deck of cards
            for suit in range(1, 5):
                for rank in range(2, 15):
                    self.pile.append(Card(rank=rank, suit=suit))

    def shuffle(self):
        random.shuffle(self.pile)

    def draw(self) -> (Card, bool):
        if self.pile:  # check if pile is empty
            return self.pile.pop(), True
        return Card(2, 1), False  # Fail soft if pile is empty: return error card

    def draw_n(self, n: int) -> list:
        cards = []
        for x in range(n):
            this_card = self.draw()
            if this_card[1]:  # check if this is a valid card
                cards.append(this_card)
        return cards

    def add_card(self, card: tuple):
        if card[1]:  # check if card is valid
            self.pile.append(card[0])

    def add_cards(self, cards: list):
        for card in cards:
            self.add_card(card)

    def empty_pile(self):
        self.pile = []

    def count(self) -> int:
        return len(self.pile)


"""
my_deck = Deck(full_pile=True)
my_deck.shuffle()
drawn_cards = []
while my_deck.pile:
    this_card = my_deck.draw()
    drawn_cards.append(this_card[0])
    print(this_card[0].suit, this_card[0].rank)
print("result of popping empty deck is: " + str(my_deck.draw()))
my_deck.pile += drawn_cards
print("Pile is back at " + str(len(my_deck.pile)) + " cards.")
"""
