stock=[{"name":"hot dog combo", "price": 1.50, "desc": "a hot dog and a drink"},
{"name":"80in TV","price":999.99,"desc":"a 4K UHD 80in Samsung TV"},
{"name":"LEGO Nissan Skyline","price":72.95,"desc":"Miniature Nissan Skyline made out of LEGO"}]   #items in stock
for index, item in enumerate(stock):
    print(index, ":", item["name"], "; $", item["price"], ";", item["desc"]) #prints list of items & their index inside stock
cart=[]  #list of items you buy
def store(cart):
    item=int(input("Please enter the index number of the item you want to purchase: "))  #asks the items from stock you want
    cart.append(stock[item])    #adds the item you input into cart
cashier=input("Are you done shopping yet? yes/no ").lower()  #asks if you are done shopping
while cashier!="yes":
    store(cart)
    cashier=input("Are you done shopping yet? yes/no ").lower()  #asks if you are done shopping
if cashier=="yes":
    def receipt(orders):
        the_receipt={}  
        for item in orders:
            if item["name"] in the_receipt: #if the item is already in the_receipt, the quantity of that item will go up by 1
                the_receipt[item['name']]['qty']+=1
            else:  #if the item isn't already in the_receipt, a dictionary inside the_receipt will be made under that item, its price, and set to a quantity of 1
                the_receipt[item['name']]={'price':item['price'],'qty':1}
        for item, value in the_receipt.items():
            price=value['price']*value['qty']   #the price of each item will be the price per item times the quantity
            print(item, price, value['qty'])    #it will print the name, total price of the specific items, the value that is the amount per item
    receipt(cart)