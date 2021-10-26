class Product():
    def __init__(self, name, price=None):
        self.name = name
        if (price is None):
            raise ValueError('Price is missing')
        else:
            self.price = price
            
class DiscountRule():
    def __init__(self, discount):
        self.discount = discount

class Checkout():
    def __init__(self):
        self.items = []
        self.discount_rules = []
        
    def add_product(self, product):
        self.items.append(product)
        
    def add_discount_rule(self, discount):
        self.discount_rules.append(discount)

    def calculate_current_total(self):
        cart_items = self.items
        cart_total = 0
        
        for item in cart_items:
            cart_total += item.price

        for rule in self.discount_rules:
            cart_discount = 0
            
            print('rule: ', rule.discount)
            
            cart_discount = cart_total * rule.discount
            
            cart_total -= round(cart_discount, 2)
            
            print('discount: ', cart_discount)

        return cart_total
        
        

        

myCheckout = Checkout()

product1 = Product('Milk', 3)

myCheckout.add_product(product1)

amount1 = DiscountRule(.05)

myCheckout.add_discount_rule(amount1)

print('Cart Total: ', '$' + str(myCheckout.calculate_current_total()))