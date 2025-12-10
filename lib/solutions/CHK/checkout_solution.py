
class CheckoutSolution:
    price_table = {
                "A": {
                    "price": 50, 
                    "deal": [3, 130]
                    },
                "B": {
                    "price": 30, 
                    "deal": [2, 45]
                    },
                "C": {
                    "price": 20
                },
                "D": {
                    "price": 15
                    }
                }
    
    # skus = unicode string
    def checkout(self, skus):
        total_cost = 0

        checkout = {}

        for sku in list(skus):
            if sku in self.price_table.keys():
                checkout[sku] = skus.count(sku)
            else:
                return -1

        for (item, count) in checkout.items():
            if self.price_table[item].get('deal'):
                total_cost += (count // self.price_table[item]['deal'][0]) * self.price_table[item]['deal'][1]
                count = count % self.price_table[item]['deal'][0]

            total_cost += count * self.price_table[item]['price']
        return total_cost

