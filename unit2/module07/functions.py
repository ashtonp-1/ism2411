#self assessment
#1. I first noticeded the calculation error in the total variable. I fixed it by changing the line to total += sale instead of total = sale. i found it from the print() as value was replaced and not added. I think it was a pretty simple patch that lets me know i at least have a minor ability in bug fixing without being tottally stuck
#2. The function apply_discount() takes a price and a tier and returns the price after applying a discount based on the tier.
#3. I did use ai for the prosses of exersize 5 and to get a better understanding of functions and how to apply them better.

#--- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate
print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0

    return price * (1 - discount)


for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(200, tier):.2f}")

#--- Exercise 3 ---

discounted_price = apply_discount(200, "gold")
tax = calculate_tax(discounted_price, 0.07)

print(f"After gold discount: ${discounted_price:.2f}")
print(f"After tax: ${discounted_price + tax:.2f}")


def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

#--- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

#--- Exercise 5 ---

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
# --- Exercise 6 ---
x = 100  # Global variable

def double_it():
    x = 999  # Local variable; does not change the global x
    return x * 2

print(x)           # Prints 100
print(double_it()) # Prints 1998
print(x)           # does not change; still prints 100

# Scope explanation:
# A local variable belongs to the function where it is created.
# Changing the local value of x does not change the global value of x.
