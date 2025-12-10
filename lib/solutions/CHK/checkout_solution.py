
class CheckoutSolution:
    price_table = {
                "A": 50,
                "B": 30, 
                "C": 20,
                "D": 15,
                "E": 40
                }
    
    deals = {
        "3A": 130,
        "5A": 200,
        "2B": 45,
        "2E": "-1B"
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

