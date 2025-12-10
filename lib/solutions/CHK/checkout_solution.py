
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
            "price": 70,
            "deals": [{"type":"multibuy", "qty":2, "price":120}]
            },
        "L": {
            "price": 90,
            "deals": []
            },
        "M": {
            "price": 15,
            "deals": []
            },
        "N": {
            "price": 40,
            "deals": [{"type":"BOGOF", "buy":3, "free_item":"M", "free_qty":1}]
            },
        "O": {
            "price": 10,
            "deals": []
            },
        "P": {
            "price": 50,
            "deals": [{"type":"multibuy", "qty":5, "price":200}]
            },
        "Q": {
            "price": 30,
            "deals": [{"type":"multibuy", "qty":3, "price":80}]
            },
        "R": {
            "price": 50,
            "deals": [{"type":"BOGOF", "buy":3, "free_item":"Q", "free_qty":1}]
            },
        "S": {
            "price": 20,
            "deals": [{"type":"group discount", "qty":3, "group":["S","T","X","Y","Z"], "price": 45}]
            },
        "T": {
            "price": 20,
            "deals": [{"type":"group discount", "qty":3, "group":["S","T","X","Y","Z"], "price": 45}]
            },
        "U": {
            "price": 40,
            "deals": [{"type":"BOGOF", "buy":3, "free_item":"U", "free_qty":1}]
            },
        "V": {
            "price": 50,
            "deals": [{"type":"multibuy", "qty":2, "price":90},
                      {"type":"multibuy", "qty":3, "price":130}]
            },
        "W": {
            "price": 20,
            "deals": []
            },
        "X": {
            "price": 17,
            "deals": [{"type":"group discount", "qty":3, "group":["S","T","X","Y","Z"], "price": 45}]
            },
        "Y": {
            "price": 20,
            "deals": [{"type":"group discount", "qty":3, "group":["S","T","X","Y","Z"], "price": 45}]
            },
        "Z": {
            "price": 21,
            "deals": [{"type":"group discount", "qty":3, "group":["S","T","X","Y","Z"], "price": 45}]
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
        
    def apply_group_discount(self, skus):
        print(f'original skus: {skus}')
        total = 0

        group_discounts = []
        for item, details in self.price_table.items():
            for deal in details['deals']:
                if deal["type"] == "group discount":
                    group_discounts.append(deal)
        
        for discount in group_discounts:
            pool = []
            for sku in discount["group"]:
                if sku in skus and skus[sku] > 0:
                    pool.append((sku, self.price_table[sku]["price"], skus[sku]))
            if not pool:
                continue

            items = []
            for sku, price, count in pool:
                items.extend([(sku, price)] * count)
            items.sort(key=lambda x: x[1], reverse=True)
            
            sets = len(items) // deal["qty"]
            total += sets * deal["price"]
            
            for i in range(sets*deal["qty"]):
                sku, price = items.pop(0)
                skus[sku] -= 1
        print(f'final skus: {skus}')

        return total

    
    # skus = unicode string
    def checkout(self, skus):
        checkout = {}

        for sku in list(skus):
            if sku in self.price_table.keys():
                checkout[sku] = skus.count(sku)
            else:
                return -1
            
        self.apply_bogof(checkout)
        total_cost = self.apply_group_discount(checkout)
        for item, count in checkout.items():
            total_cost += self.apply_multibuy(item, count)
        
        return total_cost
    
# def format_deals(item, deals):
#     new_deals = []
#     for deal in deals:
#         if deal["type"] == "multibuy":
#             new_deals.append(str(deal['qty'])+item+' for '+str(deal['price']))
#         else:
#             new_deals.append(str(deal['buy'])+item+" get "+str(deal["free_qty"])+deal["free_item"]+" free")
#     return new_deals



cs = CheckoutSolution()
SKUs = "AAABBCSXXYY"
print(cs.checkout(SKUs))
# for (item, details) in cs.price_table.items():
#     print(f'{item}\t{details['price']}, {", ".join(format_deals(item, details['deals']))}')

