#--- 3 Self-Assessment Questions ---
#1. accumulator pattern means starting with a value, adding to it as you go through a list. The three steps are initialize, update, and use the result.
#2.The while loop was longer than the for loop because I had to create and update the index myself. The for loop is simpler, while the while loop gives more control.
#3. In accounting, I could use a loop to calculate total sales from a list of sales amounts. I would add each sale to a total and print the total at the end.


#--- exercise 1 ---
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")
count = 0
for sale in sales:
    count += 1
#--- exercise 2 ---
print(f"Count: {count}")
Average = total / count
print(f"Average: ${Average:.2f}")
#--- exercise 3 ---
current_max = 0
for sale in sales:
    if sale > current_max:
        current_max = sale
print(f"Largest Sale: ${current_max}")
#-- exercise 4 ---
Sales_above_100 = 0
for sale in sales:
    if sale > 100:
        Sales_above_100 += 1
print(f"Sales above $100: {Sales_above_100}")
total_above_100 = 0
for sale in sales:
    if sale > 100:
        total_above_100 += sale
print(f"Total of Sales above $100: ${total_above_100}")
#--- exercise 5 ---
for sale in sales:
    if sale > 400:
        print(f"Alert: outlier found — ${sale}. Stopping.")
        break
    if sale <= 100:
        continue
    print(f"${sale}")
#--- exercise 6 ---
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
i = 0

while i < len(sales):
    total += sales[i]
    i += 1

print(f"Total: ${total}")

#--- exercise 7 ---
for sale in sales:
    if sale >= 200:
        discount = 0.10
    elif sale >= 100:
        discount = 0.05
    else:
        discount = 0
    discounted_price = sale * (1 - discount)
    print(f"${sale} → {discount:.0%} discount → ${discounted_price:.2f}")