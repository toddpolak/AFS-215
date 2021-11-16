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
        if (!product.price) {
            throw new Error('Empty Price')
        } else {
            this.items.push(product)
            return this.items
        }
    }

    add_discount_rule(rule) {
        this.discount_rules.push(rule)
        return this.discount_rules
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

export { Checkout, Product, DiscountRule }
