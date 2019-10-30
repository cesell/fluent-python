#%% [markdown]
# # Object Oriented Programming

import random 
#%%
class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour # calls the setter 
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        return self._hour # _ means private attribute, dont access directly

    @hour.setter
    def hour(self, hour):
        if not (0 <= hour < 24):
            raise ValueError(f'Hour ({hour}) must be 0-23')
        self._hour = hour

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, minute):
        if not (0 <= minute < 60):
            raise ValueError(f'Minutes ({minute}) must be 0-59')
        self._minute = minute

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, second):
        if not (0 <= second < 60):
            raise ValueError(f'Second ({second}) must be 0-59')

        self._second = second

    def set_time(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self):
        return (f'Time(hour={self.hour}, minute={self.minute}, ' + 
                f'second={self.second})') #similar to the constructor

    def __str__(self):
        return (('12' if self.hour in (0, 12) else str(self.hour % 12)) + 
                f':{self.minute:0>2}:{self.second:0>2}' + 
                (' AM' if self.hour < 12 else ' PM'))

#%% Using the Time Class
wake_up = Time(hour=7, minute=45, second=0)

print(wake_up)

print(wake_up._hour) # attributes are always accessible

#%% [markdown]
# ## Private Attributes

class PrivateClass:
    def __init__(self):
        self.public_data = 'public'
        self.__private_data = 'private'  #python changes the attribute name

my_object = PrivateClass()

print(my_object.public_data)
#print(my_object.__private_data) # this will raise an exception

#%% 
class Card:
    # Class Attributes
    FACES = ['Ace'] + [str(n) for n in range(2,11)] + ['Jack','Queen','King']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, face, suit):

        self._face = face
        self._suit = suit

    @property
    def face(self):
        return self._face

    @property
    def suit(self):
        return self._suit

    @property
    def image_name(self):
        return str(self).replace(' ','_') + '.png' 

    def __repr__(self):
        return f"Card(face='{self.face}', suit='{self.suit}')"

    def __str__(self):
        return f'{self.face} of {self.suit}'

    # when the object is formatted as a string, like in an f string
    def __format__(self, format):
        return f'{str(self):{format}}'

#%% 
class DeckOfCards:
    NUMBER_OF_CARDS = 52
    def __init__(self):
        self._current_card = 0
        self._deck = []

        for count in range(DeckOfCards.NUMBER_OF_CARDS):
            self._deck.append(Card(Card.FACES[count % 13], 
                                   Card.SUITS[count // 13]))
    
    def shuffle(self):
        self._current_card = 0
        random.shuffle(self._deck)

    def deal_card(self):
        try: 
            card = self._deck[self._current_card]
            self._current_card += 1
            return card
        except:
            return None

    def __str__(self):
        s = ''
        for index, card in enumerate(self._deck):
            s += f'{self._deck[index]:<19}' 
            if (index + 1) % 4 == 0:
                s += '\n'
        return s

