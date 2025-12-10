
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
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
        total_cost = 0

        skus = [skus.count(sku) for sku in list(skus) if sku in price_table.keys()]
        print(skus)

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



