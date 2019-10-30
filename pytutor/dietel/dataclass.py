from collections import namedtuple
from dataclasses import dataclass
from typing import ClassVar, List  # typing

# Named Tuples

# Data Classes
# They could become the preferred way to define many Python classes
# Among other things they autogenerate __init ,  __repr, __eq
# Regular classes define class attributes outside the methods and data attributes
# inside __init.  Data classes store both outside and need additional info

@dataclass
class Card:
    FACES : ClassVar[List[str]] = ['Ace'] + \
                                  [str(n) for n in range(2,11)] + \
                                  ['Jack','Queen','King']
    SUITS : ClassVar[List[str]] = ['Hearts','Diamonds','Clubs','Spades']

    face: str
    suit: str

    @property
    def image_name(self):
        """Return the Card's image file name."""
        return str(self).replace(' ', '_') + '.png'

    def __str__(self):
        """Return string representation for str()."""
        return f'{self.face} of {self.suit}'
    
    def __format__(self, format):
        """Return formatted string representation."""
        return f'{str(self):{format}}'



#%%
if __name__ == '__main__':

    CardTuple = namedtuple('Card', ['face', 'suit'])

    card = CardTuple(face='Ace', suit='Spades')

    print(f'{card.face} of {card.suit}')

    # useful technique is reading CSV files

    card = CardTuple._make(['Queen','Heart'])
    print(f'{card.face} of {card.suit}')

    c1 = Card(face='Ace', suit='Spades')
    c2 = Card(Card.FACES[0], Card.SUITS[3])
    c3 = Card(Card.FACES[0], Card.SUITS[0])

    print(c1, c1.image_name)
    print(f'c1 == c2 : {c1==c2}')
    print(f'c1 == c3 : {c1==c3}')
#%%
