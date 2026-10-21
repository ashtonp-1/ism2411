#---- 3 Self-Assessment Questions----
# 1. In exercise 6 if i forgot to divide by 100 python would not crash but have a silent error 

#2 . % finds the remainder of an operationn, another business use could be shipping trucks. One truck can hold 200 boxes, but there are 1300 boxes in total. 

# 3.The concept im leaset comforable with if the f-strings, i have to be very aware of the way im typing them out


# --- Exercise 1 ---
# revenue, discounts and calculator
price = 50
quantity = 12
revenue = price * quantity

print(f"Revenue: ${revenue:,.2f}")

#--- Exersize 3 ---
cost = 32
price = 50 
margin = (price - cost) / price
print (f"Margin {margin:.1%}")

#--- Exersize 3 ---
margin_a =.6
margin_b =.25
product_a_wins = margin_a > margin_b
print(f" Product A wins: {product_a_wins}")



#---- Exersize 4 ----

is_premium = price > 100 and margin > 0.3
print (f"Is Premium: {is_premium}")

price = 150
margin = .35

#--- Exersize 5 ----

print (17/5)  #complete 
# True division fully does the operation
print (19//5) #floor
# Rounds down to the next full number
print (17%5)  #mod
#

#--- Exsersize 6 ----

product = input("Enter the product name: ")
retail_price = float(input("Enter the retail price: "))
quantity_sold = int(input("Enter the quantity: "))
discount_pct = int(input("Enter the discount rate: "))
cost = float(input("Enter the cost: "))
print("="*50)

revenue = retail_price * quantity_sold
discount_rev = revenue * (1 - discount_pct / 100)
gross_margin = (retail_price - cost) / retail_price

net_profit = discount_rev - (cost * quantity_sold)

#output
print(f"product: {product}")
print(f"Revenue: ${revenue:,.2f}")
print(f"Discounted Revenue: ${discount_rev:,.2f}")
print(f"Gross Margin: {gross_margin:.1%}")
print(f"Net Profit: ${net_profit:,.2f}")





#--- Exersize 7 ---- 
BOX_SIZE = 24
item_oredered = int (input({"number of items ordered: "}))
full_boxes = item_oredered // BOX_SIZE
loose_items = item_oredered % BOX_SIZE
exact_fit = loose_items == 0


print(f"full boxes: {full_boxes}")
print(f"loose items: {loose_items}")
print(f"exact fit: {exact_fit}")

