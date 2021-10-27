class Product():
    def __init__(self, name, price=None):
        self.name = name
        if (price is None):
            raise ValueError('Price is missing')
        else:
            self.price = price
            
class DiscountRule():
    def __init__(self, product, discount):
        self.product = product
        self.discount = discount

class Checkout():
    def __init__(self):
        self.items = []
        self.discount_rules = []
        
    def add_product(self, product):
        self.items.append(product)
        
    def add_discount_rule(self, rule):
        self.discount_rules.append(rule)

    def calculate_current_total(self):
        cart_items = self.items
        cart_total = 0
        
        for item in cart_items:
            cart_total += item.price

        return cart_total
    
    def apply_discount(self):
        cart_items = self.items
        discount_total = 0

        for rule in self.discount_rules:
            for item in cart_items:
                if item.name == rule.product:
                    discount_total += rule.discount
                    break
    
        return int(self.calculate_current_total()) - discount_total