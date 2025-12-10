
class CheckoutSolution:
    price_table = {
                "A": {
                    "price": 50, 
                    "deal": [[3, 130],
                             [5, 200]]
                    },
                "B": {
                    "price": 30, 
                    "deal": [[2, 45]]
                    },
                "C": {
                    "price": 20
                },
                "D": {
                    "price": 15
                    },
                "E": {
                    "price": 40
                    }
                }
    
    deals = {
        "3A": 130,
        "5A": 200,
        "2B": 45,
        "2E": "-B"
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

        print(list(self.deals.items())[::-1])

        # for (req, discount) in self.deals.items()[::-1]:


        for (item, count) in checkout.items():
            # if self.price_table[item].get('deal'):
            #     total_cost += (count // self.price_table[item]['deal'][0]) * self.price_table[item]['deal'][1]
            #     count = count % self.price_table[item]['deal'][0]

            total_cost += count * self.price_table[item]['price']
        return total_cost


cs = CheckoutSolution()
sku = "ABCDAEBCDABE"
print(cs.checkout(sku))

# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+