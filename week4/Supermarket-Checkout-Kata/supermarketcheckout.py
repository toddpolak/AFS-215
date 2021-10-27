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

        #for rule in self.discount_rules:
            #cart_discount = 0
            
            #print('rule: ', rule.discount)
            
            #cart_discount = cart_total * rule.discount
            
            #cart_total -= round(cart_discount, 2)
            
            #print('discount: ', cart_discount)

        return cart_total
    
    def apply_discount(self):
        cart_items = self.items
        discount_total = 0
        #cart_total = 0
        
        for rule in self.discount_rules:
            print('product: ', rule.product)
            print('discount: ', rule.discount)
        
            for item in cart_items:
                print('name: ', item.name)
                print('price: ', item.price)
        
                if item.name == rule.product:
                    discount_total += rule.discount
                    break
                    
        print('Discount Total: ', discount_total)
        print('Prev Total: ', self.calculate_current_total())
        
        return int(self.calculate_current_total()) - discount_total
        
        
        

myCheckout = Checkout()

product1 = Product('Milk', 3)

myCheckout.add_product(product1)

rule1 = DiscountRule('Milk', .25)

myCheckout.add_discount_rule(rule1)

print('Cart Total: ', '$' + str(myCheckout.calculate_current_total()))

print('New Total: ', myCheckout.apply_discount())