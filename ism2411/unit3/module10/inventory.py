print("self reflection:")
#1 I did not know about mutable and immutable types in Python. I thought if you had a list you didnt want to change you just didnt change it
#2 Searhcing through a big sheet just to change a few things. I python you can just use append() and remove() or clone the list and edit that one.

print("Exercise 1:")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("Exercise 2:")
print(inventory[0])
print(inventory[-1])
middle_index = len(inventory) // 2
print(inventory[middle_index])

print("Exercise 3:")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2]) #step slice printing evey other item

print("Exercise 4:")
inventory.append("envelope")
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

print("Exercise 5:")
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError: {error}")
    print("Tuples are immutable, meaning they protect the coordinates from being changed.")

print("Exercise 6:")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total sales: {total}")
print(f"number of sales: {count}")
print(f"Average sales: {average}")
print("Best sale:", max(sales))
print("Worst sale:", min(sales))


best = sales[0]
worst = sales[0]

for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount

print(f"Best sale: {best}")
print(f"Worst sale: {worst}")

print("Exercise 7:")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))  # Apply a 10% discount rounds 2 decimal places
print(f"Original prices: {prices}")
print(f"Discounted prices: {discounted}")

print("Exercise 8:")

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print(f"High sales: {high_sales}")
print(f"Number of high sales: {len(high_sales)}")
print(f"count: {len(high_sales)}")
print(f"average: {sum(high_sales) / len(high_sales)}")
