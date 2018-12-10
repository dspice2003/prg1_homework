from deck import deck
from card import card

class player():
    def __int___(self):
        self.score = 0
        self.hand = deck()
    def draw_card(self,drawPile):
        card = drawPile.draw()
        self.cards.remove(draw_card)
        return draw_card(card)
    def ask_card(self,opponent_deck,drawPile,card):
        cardFound = False
        for opponent_card in opponent_deck.cards:
            if(opponent_card.rank == card.rank):
                self.hand.add_card(opponent_card)
                opponent_deck.deck.remove(opponent_card)
                cardFound = True
        if(cardFound == False):
            self.draw_card(drawPile)

    def increase_score(self,discardDeck):
        pass