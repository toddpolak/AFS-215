class Product {
    constructor(name, price) {
        this.name = name
        this.price = price
    }
}

class DiscountRule {
    constructor(product, discount) {
        this.product = product
        this.discount = discount
    }
}

class Checkout {
    constructor() {
        this.items = []
        this.discount_rules = []
    }

    add_product(product) {
        this.items.push(product)
    }

    add_discount_rule(rule) {
        this.discount_rules.push(rule)
    }

    calculate_current_total() {
        let cart_total = 0

        this.items.forEach(item => {
            cart_total += item.price
        });

        return cart_total
    }

    apply_discount() {
        let discount_total = 0

        this.discount_rules.forEach(rule => {
            this.items.forEach(item => {
                if (item.name === rule.product) {
                    discount_total += rule.discount
                }
            })
        })

        return this.calculate_current_total() - discount_total
    }
}

let myCheckout = new Checkout()
let myProduct = new Product('Milk', 3)
let myDiscount = new DiscountRule('Milk', .25)

myCheckout.add_product(myProduct)

console.log(myCheckout.items)
console.log(myCheckout.calculate_current_total())

myCheckout.add_discount_rule(myDiscount)

console.log(myCheckout.apply_discount())

