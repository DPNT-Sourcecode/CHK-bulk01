
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
                        {"type":"BOGOF", "buy":2, "free_item":"B", "free_qty":1},
                    ]
                    },
                "F": {
                    "price": 10,
                    "deals": [
                        {"type":"BOGOF", "buy":2, "free_item":"F", "free_qty":1},
                    ]
                    }
                }
    
    def apply_multibuy(self, item, qty):
        total = 0
        deals = [deal for deal in self.price_table[item]['deals'] if deal['type'] == "multibuy"]

        deals.sort(key=lambda d: d["qty"], reverse=True)

        total = 0
        for deal in deals:
            total += (qty // deal['qty']) * deal["price"]
            qty -= (qty // deal['qty']) * deal["qty"]
        total += qty * self.price_table[item]
        return total
    
    def apply_bogof(self, skus):
        for item, details in self.price_table.items():
            for deal in details["deals"]:
                if deal["type"] != "BOGOF" or item not in skus:
                    continue

            requirement = deal["buy"]
            
            triggers = skus[item] // requirement

            if deal["free_item"] in skus:
                skus[deal["free_item"]] -= triggers
                if skus[deal["free_item"]] < 0:
                    skus[deal["free_item"]] = 0
    
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
            
        self.apply_bogof(skus)
        for item, count in skus.items():
            total_cost += self.apply_multibuy(item, count)
        
        return total_cost
    

cs = CheckoutSolution()
SKUs = ""
print(cs.checkout(SKUs))

