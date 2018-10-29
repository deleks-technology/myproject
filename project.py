print ("Welcome to CodeLagos Super Market!!")
print ("==============================================")

#=============Stating the Various List================================
item_number = int(input("How many products will you like to input today:"))
shop_list=[]
stock=[]
price=[]
sale=[]

#=================First Loop==========================================
for i in range(item_number):
    shop_input= input("Enter the name of product %s:" %(i+1))
    shop_list.append(shop_input)
    print("===========================================================")
    stock_input = int(input("Enter the number of product %s in stock:" %(shop_input)))
    stock.append(stock_input)
    print("===========================================================")
    costPrice_input = float(input("Enter the cost price of product %s:" %(shop_input)))
    price.append(costPrice_input)
    print("===========================================================")
    salePrice_input = float(input("Enter the selling price of product %s:" %(shop_input)))
    sale.append(salePrice_input)
    print("===========================================================")
#=============================Getting each element in our shopping list===================
    for n in shop_list:
        print("Shop List:")
        print(n)
        print("=============================================================================")
#=============================Getting each element in our stock list===================
for m in stock:
    print("Stock List:")
    print(m)
    print("=============================================================================")
#=============================Getting each element in our price list===================
for o in price:
    print("Price List:")
    print(o)
    print("=============================================================================")
#=============================Getting each element in our sales list===================
for p in sale:
    print("Our Sales List")
    print (p)
    print("=============================================================================")
#==================================Calculation Logic================================================
for a in range(item_number):
    total = 0
    loss = 0
    if stock[a] > 0 and sale[a] < price[a]:
        loss = price[a] - sale[a]
        loss = stock[a] * loss
        a+=1
        print("You have made a loss of: ", loss)
        print("===================================================================================")

    elif stock[a] > 0 and sale[a] > price[a]:
        total = stock[a] * sale[a]
        profit = stock[a] * (sale[a] - price[a])
        a+=1
        print("The total selling price of the product %s after sales you enter is %s" %((a), total))
        print("====================================================================================")
        print("The total profits of the product %s made after sales is %s" %(a, profit))
        print("====================")
     
    # else:
        print("%s is out of stock!" %(shop_input))

    
        

