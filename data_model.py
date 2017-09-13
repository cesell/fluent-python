'''
The Python interpreter invokes special methods to perform basic object oper‐
ations, often triggered by special syntax. The special method names are always spelled
with leading and trailing double underscores, i.e. __getitem__. For example, the syntax
obj[key] is supported by the __getitem__ special method. 

TIP: The term magic method is slang for special method, but when talk‐
ing about a specific method like __getitem__say “dunder-getitem”. 
'''

# the following code shows how to implement __getitem__ and __len__

import collections

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]


    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

def using_FrenchDeck():

    from random import choice

    deck = FrenchDeck()
    print('''
    Using special methods to leverage the Python Data Model:\n
    1. Don’t have to memorize arbitrary method names for standard operations \n
    2. It’s easier to benefit from the rich Python standard library and avoid \n
    reinventing the wheel. We have:
    ''')
    print('The len {}'.format(len(deck)),end='\n\n')
    print('A random card {}'.format(choice(deck)),end='\n\n')
    print('Slicing {}'.format(deck[:3]),end='\n\n')
    print('__getitem__ makes the deck iterable',end='\n\n')
    for card in deck:
        print(card)
    print('and in reverse order')
    for card in reversed(deck):
        print(card)
    print('or searchable Card("Q","hearts") in deck {}'.format(Card("Q","hearts") in deck),end='\n\n')

    print('or you can add your own sorting method',end='\n\n')

    for card in sorted(deck, key=spades_high):
        print(card)

from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        #choose __repr__, because when no custom __str__ Python will call __repr__
        #return 'Vector(%r,%r)' % (self.x,self.y)
        return 'Vector({},{})'.format(self.x,self.y)

    def __abs__(self):
        return hypot(self.x,self.y)

    def __bool__(self):
        '''
        returns False if the maggitude of the vector is zero, True otherwise. 
        '''
        return bool(abs(self))
        #return bool(self.x or self.y)


    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __mul__(self,scalar):
        return Vector(self.x*scalar, self.y*scalar)


def usingVector():

    print(''' 
    Using a class that implements: 
    __repr__, __abs__, __add__ and __mul__:
    ''')
    v1 = Vector(2,4)
    v2 = Vector(2,1)
    v = v1 + v2
    print('{} + {} = {}'.format(v1,v2,v))
    print('abs({}) = {}'.format(v,abs(v)))
    print('{} * 3 = {}'.format(v,v * 3))

'''
Why len is not a method
I asked this question to core developer Raymond Hettinger in 2013 and the key to his
answer was a quote from the Zen of Python: “practicality beats purity”. In “How special
methods are used” on page 8 I described how len(x) runs very fast when x is an instance
of a built-in type. No method is called for the built-in objects of CPython: the length is
simply read from a field in a C struct. Getting the number of items in a collection is a
common operation and
'''


if __name__== '__main__':
    using_FrenchDeck()
    usingVector()
