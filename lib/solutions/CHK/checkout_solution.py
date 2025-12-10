
class CheckoutSolution:
    price_table = {
                "A": {
                    "price": 50, 
                    "deal": ''
                    },
                "B": {
                    "price": 30, 
                    "deal": ''
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

        for (item, count) in skus.items():
            if self.price_table[item].deal:
                

        return total_cost


cs = CheckoutSolution()
sku = "ABCDABCDAB"
print(cs.checkout(sku))

# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+




