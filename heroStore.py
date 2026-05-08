stock=[{"name":"hot dog combo", "price": 1.50, "desc": "a hot dog and a drink"},
{"name":"Lightsaber+","price":99999.99,"desc":"an upgraded lightsaber"},
{"name":"Shield of Gliberglop","price":72.95,"desc":"a non-Newtonian shield"}]   #items in stock
for index, item in enumerate(stock):
    print(index, ":", item["name"], "; $", item["price"], ";", item["desc"]) #prints list of items & their index inside stock
class Hero:
    def __init__(self, name, money, cart=[]):
        self.name = name
        self.money = money
        self.cart=cart
    def store(self, item, cart=[]):
        self.item=item
        item=int(input("Please enter the index number of the item you want to purchase: "))  #asks the items from stock you want
        cart.append(stock[item])    #adds the item you input into cart
Jillian = Hero("Jillian", 150, ["Potion"])
cashier=input("Are you done shopping yet? yes/no ").lower()  #asks if you are done shopping
while cashier!="yes":
    Jillian.store("",)
    cashier=input("Are you done shopping yet? yes/no ").lower()  #asks if you are done shopping
if cashier=="yes":
    def receipt(orders):
        the_receipt={}  
        for item in orders:
            if item['name'] in the_receipt: #if the item is already in the_receipt, the quantity of that item will go up by 1
                the_receipt[item['name']]['qty']+=1
            else:  #if the item isn't already in the_receipt, a dictionary inside the_receipt will be made under that item, its price, and set to a quantity of 1
                the_receipt[item['name']]={'price':item['price'],'qty':1}
        for item, value in the_receipt.items():
            price=value['price']*value['qty']   #the price of each item will be the price per item times the quantity
            print(item, price, value['qty'])    #it will print the name, total price of the specific items, the value that is the amount per item
    print(receipt(Jillian.cart))