
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

        skus = [skus.count(sku) for sku in skus.split() if sku in price_table.keys()]

        return total_cost


# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+


