import random

class Card(object):

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __cmp__(self, other):
        # check the ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # ranks are the same, so check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # suits and ranks are the same, so tie
        return 0

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    def pop_card(self):
        return self.cards.pop()
    def add_card(self, card):
        self.cards.append(card)
    def shuffle(self):
        random.shuffle(self.cards)
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

        
class Hand(Deck):
    ''' Hand inherits from Deck. '''
    def __init__(self,label=''):
        self.cards = []
        self.label = label
    def has_pair(self):
        res = []
        result = False
        for card in self.cards:
            res.append(card.rank)
            for i in res:
                res.count(i)
                if res.count(i) >= 2:
                    result = True
        return result
    def has_twopair(self):
        res = []
        result = False
        for card in self.cards:
            res.append(card.rank)
            res2 = []
            for i in res:
                res2.append(res.count(i))
                n = 0
                for second_i in res2:
                    if second_i == 2:
                        n = n+1
                        if n >= 4:
                            result = True
        return result
    def has_flush(self, num):
        res = []
        result = False
        for card in self.cards:
            res.append(card.suit)
            for i in res:
                res.count(i)
                print res
                res = [2,2,2,2,2]
                if res.count(i) == num:
                    result = True
        return result

       

d = Deck()
h = Hand()
d.shuffle()
d.move_cards(h,7)
print h
print
print h.has_pair()
print h.has_twopair()
print h.has_flush(5)
