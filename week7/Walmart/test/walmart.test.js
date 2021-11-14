import { assert, expect } from 'chai'
import { Checkout, Product, DiscountRule } from '../walmart.js'

describe('Run Tests', () => {

    let myCheckout

    it('Can create an instance of the Checkout class', () => {
        myCheckout = new Checkout()

        assert.isDefined(myCheckout.items = [])

        expect(myCheckout).to.have.property('items').and.to.be.an('array')
    })

    it('Can add an item & price', () => {

        assert.deepEqual(myCheckout.add_product(new Product('Milk', 3)), 
            [{name: 'Milk', price: 3}])
    })

    it('Can calculate the current total', () => {
        assert.equal(myCheckout.calculate_current_total(), 3)
    })

    it('Can add multiple items and get correct total', () => {

        assert.deepEqual(myCheckout.add_product(new Product('Bread', 1.5)), 
            [{name: 'Milk', price: 3}, 
            {name: 'Bread', price: 1.5}])

        assert.deepEqual(myCheckout.add_product(new Product('Eggs', 2)), 
            [{name: 'Milk', price: 3}, 
            {name: 'Bread', price: 1.5}, 
            {name: 'Eggs', price: 2}])

        assert.equal(myCheckout.calculate_current_total(), 6.5)

    })

})






