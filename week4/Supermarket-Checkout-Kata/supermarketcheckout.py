class Product():
    def __init__(self, name, price=None):
        self.name = name
        if (price is None):
            raise ValueError('Price is missing')
        else:
            self.price = price

class Checkout():
    def __init__(self):
        self.items = []
        
    def add_product(self, product):
        self.items.append(product)
        
    def calculate_current_total(self):
        cart_items = self.items
        cart_total = 0
        
        for item in cart_items:
            cart_total += item.price
            
        return cart_total
        
        

        

#myCheckout = Checkout()

#product1 = Product('Milk', 3)

#myCheckout.add_product(product1)

#print('Cart Total: ', '$' + str(myCheckout.calculate_current_total()))