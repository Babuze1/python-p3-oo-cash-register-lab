#!/usr/bin/env python3

class CashRegister:
    def __init__(self):
        self.items = []
        self.total_price = 0
        self.last_transaction = 0
    
    def add_item(self, price, quantity=1):
        self.total_price += price * quantity
        self.last_transaction = price * quantity
        self.items.append({'price': price, 'quantity': quantity})
    
    def apply_discount(self, discount_percentage):
        discount = (discount_percentage / 100) * self.total_price
        self.total_price -= discount
        return self.total_price
    
    def void_last_transaction(self):
        if self.items:
            self.total_price -= self.last_transaction
            self.items.pop()
            if self.items:
                self.last_transaction = self.items[-1]['price'] * self.items[-1]['quantity']
            else:
                self.last_transaction = 0
        else:
            self.last_transaction = 0
    
    def get_total(self):
        return self.total_price
