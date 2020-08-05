from Player import Player
from Deck import Deck
from Plotter import plot_scores


class GameMaster:
    def __init__(self, verbose: bool = False, plot: bool = False):
        self.player1 = Player()
        self.player2 = Player()
        self.deck = Deck(full_pile=True)
        self.deck.shuffle()
        self.deal_cards()
        self.war_size: int = 3
        self.round: int = 1
        self.verbose = verbose
        self.plot = plot

    def deal_cards(self):
        while self.deck.count() > 0:
            self.player1.take_card(self.deck.draw())
            self.player2.take_card(self.deck.draw())

    @staticmethod
    def valid_hand(card1: tuple, card2: tuple):
        if not (card1[1] and card2[1]):
            raise Exception("\nAn invalid card was played!\n")

    def declare_round(self):
        if self.verbose:
            print("\nRound " + str(self.round) + ": Score is " + str(self.player1.score()) + " to " + str(
                self.player2.score()))

    def declare_cards(self, card1: tuple, card2: tuple):
        if self.verbose:
            print("\t" + card1[0].declare_name() + " vs. " + card2[0].declare_name())

    def declare_war_cards(self, cards1: list, cards2: list):
        if self.verbose:
            print("\tWAR! " + str(len(cards1)) + " cards vs. " + str(len(cards2)) + " cards")
            self.declare_cards(cards1[-1], cards2[-1])

    def play_round(self):
        player1_card = self.player1.play_card()
        player2_card = self.player2.play_card()
        self.declare_cards(player1_card, player2_card)
        self.valid_hand(player1_card, player2_card)
        pot = [player1_card, player2_card]
        if player1_card[0].rank == player2_card[0].rank:
            if self.player1.score() <= 0:  # account for this tie being a players' final card
                self.player2.take_cards(pot)
            elif self.player2.score() <= 0:
                self.player1.take_cards(pot)
            else:
                self.play_war(pot, self.war_size)
        elif player1_card[0].rank > player2_card[0].rank:
            self.player1.take_cards(pot)
        else:
            self.player2.take_cards(pot)
        self.player1.update_record(self.round)
        self.player2.update_record(self.round)

    def play_war(self, cards: list, n: int):
        player1_cards = self.player1.play_war(n)
        player2_cards = self.player2.play_war(n)
        self.declare_war_cards(player1_cards, player2_cards)
        self.valid_hand(player1_cards[-1], player2_cards[-1])
        pot = cards + player1_cards + player2_cards
        player1_war_rank = player1_cards[-1][0].rank
        player2_war_rank = player2_cards[-1][0].rank

        if player1_war_rank == player2_war_rank:
            self.play_war(pot, n)
        elif player1_war_rank > player2_war_rank:
            self.player1.take_cards(pot)
        else:
            self.player2.take_cards(pot)
        self.player1.update_record(self.round)
        self.player2.update_record(self.round)

    def play_game(self):
        while self.player1.score() > 0 and self.player2.score() > 0:
            self.declare_round()
            self.play_round()
            self.round += 1
        print("\n\nGame finished after " + str(self.round-1) + " rounds.")
        if self.plot:
            plot_scores(self.player1.record, self.player2.record, self.round)
