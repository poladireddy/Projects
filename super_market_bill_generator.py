from datetime import datetime

name = input("enter your name:")

lists ='''
brush Rs 20 per piece
Bottle Rs30 per piece
Rice   Rs 50/kg
Sugar  Rs 40/kg
Salt   Rs 20/kg
oil    Rs 90/liter
paneer Rs 150/kg
maggi  Rs 50/kg
milk   Rs 25/kg
boost  Rs 60/kg
pulses Rs 100/kg
cooldrink  Rs 80/lit
soaps Rs 30/each
flour Rs 40/kg
'''
#declaration
price = 0
pricelist = []
totalprice = 0
Finalfinalprice = 0
ilist = []
qlist = []
plist = []

#rates for items
items = {"rice":50,"sugar":40,
"oil":90,"paneer":150,
"maggi":50,"boost":60,
"soap":30,"flour":40,
"cooldrink":80,"pulses":100}

#selecting an item through keys
option = int(input("for list of item please press 1:"))
if option == 1:
    print(lists)
for i in range(len(items)):
    inp1 = int(input("if u want to buy press 1 or press 2 to exit:"))  #to buy press 1
    if inp1 == 2:
        break
    if inp1 == 1:
        item =input("enter your items:")
        quantity = int(input("enter your quantity:"))
        if item in items.keys():
            price = quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst = (totalprice*5)/100
            finalamount = gst+totalprice
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number")
    inp = input('can I bill the the items yes or no:')
    if inp == "yes":
            print("="*30,"TEJAREDDY MARKET","="*30)
            print(50*" ","Hanamkonda")
            print(50*"-")
            print("\n")
            print("Name:",name,30*" ","Date:",datetime.now())
            print("\n")
            print("sno",2*" ","items",8*" ","Quantity",5*" ","price")

            for i in range(len(pricelist)):
                print(i,4*" ",ilist[i],12*" ",qlist[i],8*" ",plist[i],"Rs/-",)

            print(75*"-")
            print(50*" ","TotalAmount:",totalprice,"Rs/-",50*"")
            print("gst amount",50*" ",gst,"Rs/-")
            # print("\n")#new line
            print(75*"-")
            print(50*" ","finalamount:",finalamount,"Rs/-",50*" ")
            print(75*"-")
            print(25*" ","Thanks for visiting",25*" ")
            print(75*"-")

            # print(i,list[i],qlist[i],plist[i])




# print("-"*30,"KiarnOruganti supermarket","-"*30)
# print(50*" ","Hanamkonda")
# print(50*"-")
# print("\n")
# print("Name:",name,30*" ","Date:",datetime.now())
# print("\n")
# print("sno",2*" ","items",8*" ","Quantity",5*" ","price")

# for i in range(len(pricelist)):
#     print(i,4*" ",ilist[i],12*" ",qlist[i],8*" ",plist[i],"Rs/-",)

#     print(75*"-")
#     print(50*" ","TotalAmount:",totalprice,"Rs/-",50*"")
#     print("gst amount",50*" ",gst,"Rs/-")
#     # print("\n")#new line
#     print(75*"-")
#     print(50*" ","finalamount:",finalamount,"Rs/-",50*" ")
#     print(75*"-")
#     print(25*" ","Thanks for visiting",25*" ")
# print(75*"-")
print(price)