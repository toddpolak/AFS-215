from supermarketcheckout import Product, DiscountRule, Checkout
import pytest

myCheckout = Checkout()

def test_Instantiate():
    assert type (myCheckout) is Checkout
    
def test_AddItem():
    myCheckout.add_product(Product('Milk', 3))
    
def test_CalculateCurrentTotal():
    total = myCheckout.calculate_current_total()
    assert total == 3
    
def test_AddMultipleItems():
    myCheckout.add_product(Product('Eggs', 2))
    myCheckout.add_product(Product('Meat', 5))
    myCheckout.add_product(Product('Cereal', 3))
    
def test_RecalculateCurrentTotal():
    total = myCheckout.calculate_current_total()
    assert total == 13
    
def test_AddDiscountRule():
    myCheckout.add_discount_rule(DiscountRule('Milk', .25))
    
def test_ApplyDiscount():
    total = myCheckout.apply_discount()
    assert total == 12.75
    
def test_exception_AddWithoutPrice():
    with pytest.raises(Exception) as e_info:
        myCheckout.add_product(Product('Bread'))
    