# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale #calculation error; should be total += sale, not just =
print(f"Total: ${total}")

count = 0
for sale in sales: #missing colon at the end of the for loop
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales): #you only need < len(sales) using <= will cause an index error outside of the list range; which is 0 to 4
    print(sales[i])
    i += 1
