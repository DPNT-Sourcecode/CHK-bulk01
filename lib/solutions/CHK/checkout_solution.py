
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
            },
        "G": {
            "price": 20,
            "deals": []
            },
        "H": {
            "price": 10,
            "deals": [{"type":"multibuy", "qty":5, "price":45},
                      {"type":"multibuy", "qty":10, "price":80}]
            },
        "I": {
            "price": 35,
            "deals": []
            },
        "J": {
            "price": 60,
            "deals": []
            },
        "K": {
            "price": 80,
            "deals": [{"type":"multibuy", "qty":2, "price":150}]
            },
        "L": {
            "price": 90,
            "deals": []
            },
        "M": {
            "price": 15,
            "deals": [{"type":"BOGOF", "buy":3, "free_item":"M", "free_qty":}]
            },
        "N": {
            "price": 40,
            "deals": []
            },
        "O": {
            "price": 10,
            "deals": []
            },
        "P": {
            "price": 50,
            "deals": []
            },
        "Q": {
            "price": 30,
            "deals": []
            },
        "R": {
            "price": 50,
            "deals": []
            },
        "S": {
            "price": 30,
            "deals": []
            },
        "T": {
            "price": 20,
            "deals": []
            },
        "U": {
            "price": 40,
            "deals": []
            },
        "V": {
            "price": 50,
            "deals": []
            },
        "W": {
            "price": 20,
            "deals": []
            },
        "X": {
            "price": 90,
            "deals": []
            },
        "Y": {
            "price": 10,
            "deals": []
            },
        "Z": {
            "price": 50,
            "deals": []
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
        total += qty * self.price_table[item]['price']
        return total
    
    def apply_bogof(self, skus):
        for item, details in self.price_table.items():
            for deal in details["deals"]:
                if deal["type"] != "BOGOF" or item not in skus:
                    continue

                if deal["free_item"] == item:
                    total_combo = deal["buy"] + deal["free_qty"]
                    combos = skus[item] // total_combo
                    skus[item] -= combos * deal["free_qty"]
                elif deal["free_item"] in skus:
                    skus[deal["free_item"]] -= (skus[item] // deal["buy"])
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
            
        self.apply_bogof(checkout)
        for item, count in checkout.items():
            total_cost += self.apply_multibuy(item, count)
        
        return total_cost

