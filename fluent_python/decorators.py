from collections import namedtuple
from promotions import *

Customer = namedtuple('Customer','name fidelity')

class LineItem:

    def __init__(self,product,quantity,price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

    def __repr__(self):
        fmt = '<Line Product {} Quantity {:.2f} Price {:.2f}>'
        return fmt.format(self.product, self.quantity, self.price)


class Order:  #the Context

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self,'__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due {:.2f}>'
        return fmt.format(self.total(), self.due())




if __name__ == '__main__':

    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, .5),
            LineItem('apple', 10, 1.5),
            LineItem('watermelon', 5, 5.0)]
    banana_cart = [LineItem('banana', 30, .5),
                   LineItem('apple', 10, 1.5)]
    long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]

    carts = zip([cart, banana_cart, long_order],['simple cart', 'banana_cart', 'big_cart'])
    for cart, name in carts:
        print('If joe buys the {} his order (with he best discount) would be {}'.
              format(name, Order(joe,cart,best_promo)))


