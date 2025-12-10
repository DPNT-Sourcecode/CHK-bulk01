
class CheckoutSolution:
    price_table = {
                "A": {
                    "price": 50, 
                    "deals": [
                        {"type":"multibuy", "qty":3, "price":130},
                        {"type":"multibuy", "qty":5, "price":200}
                    ]
                    },
                "B": {
                    "price": 30, 
                    "deals": [
                        {"type":"multibuy", "qty":2, "price":45}
                    ]
                    },
                "C": {
                    "price": 20,
                    "deals": []
                },
                "D": {
                    "price": 15,
                    "deals": []
                    },
                "E": {
                    "price": 40,
                    "deals": [
                        {"type":"BOGOF", "buy":2, "price":45},
                    ]
                    }
                }
    
    # skus = unicode string
    def checkout(self, skus):
        total_cost = 0

        checkout = {
                "A": 0,
                "B": 0, 
                "C": 0,
                "D": 0,
                "E": 0
                }

        for sku in list(skus):
            if sku in self.price_table.keys():
                checkout[sku] = skus.count(sku)
            else:
                return -1
            
        for (req, discount) in list(self.deals.items())[::-1]:
            count = int(req[:-1])
            item = req[-1]
            if type(discount) == int:
                total_cost += (checkout[item] // count) * discount
                checkout[item]  = checkout[item] % count
            else:
                for i in range(checkout[item] // count):
                    count = int(discount[:-1])
                    item = discount[-1]
                    checkout[item] += count
                    if checkout[item] < 0:
                        checkout[item] = 0

        for (item, count) in checkout.items():
            total_cost += count * self.price_table[item]
        return total_cost
