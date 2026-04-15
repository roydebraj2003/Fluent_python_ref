""" Example 1-1 is simple, but it demonstrates the power of implementing just two spe‐
cial methods, __getitem__ and __len__. """

import collections
from random import choice
Card = collections.namedtuple('Card', ['rank', 'suite'])

""" The Python interpreter invokes special methods to perform basic object
operations, often triggered by special syntax. The special method names are always
written with leading and trailing double underscores """

class FrenchDeck:
    ranks = [x for x in range(2, 11)] + list('JQKA')
    suite = 'hearts spades club diamond'.split()
    def __init__(self) -> None:
        self._cards = [Card(x, y) for x in self.ranks
                                  for y in self.suite]
    def __getitem__(self, postion):
        return self._cards[postion]
    def __len__(self):
        return len(self._cards)
deck = FrenchDeck()
""" The deck is iterable just by implementing __getitem__ and also allows string slicing """
for card in deck:
    print(card)
# If a collection has no __contains__ method, the in operator does a sequential scan
print(Card('A', 'spades') in deck) #True
print(Card('10', 'okok') in deck) #False
print(len(deck))
print(deck[0])
print(choice(deck))
#To sort the deck - 0 for 2 of clubs and 51 for ace of spades

suite_ranks = dict(spades=3, hearts=2, diamond=1, club=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suite_ranks)+ suite_ranks[card.suite]

for card in sorted(deck, key=spades_high):
    print(card)
