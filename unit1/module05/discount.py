#--- self assessment questions ---
# 1. It check if the total is greater than 500 and == region south, then checks if its just greater than 500, the next check is if its greater than 200 and == region south, ending at the basic > 200 check.
# 2. total > 100 is looking for anything greater than that, while total < 500 looks for the opposite. the would only produce the same results with the range of 101 - 499 because it would satisfy both conditions.
# 3. I encounter tiered conditional logic in everyday life with things like shipping fees and discounts. For example, a store might offer free shipping if you spend over $100, a smaller fee if you spend $50–$99, and a higher fee if you spend less than $50. Knowing Python conditionals helps me understand that these systems are basically checking different conditions and applying the correct result. It makes these systems seem less complicated because I can see how rules like if, elif, and else can be used to make decisions.


#--- exercise 1 ---

region = input("Enter region (north, south, east, west): ").lower()

total = float(input("Enter cart total: $"))

if total >= 500 and region == "south":
    discount = 0.17

elif total >= 500:
    discount = 0.15

elif total >= 200 and region == "south":
    discount = 0.12

elif total >= 200:
    discount = 0.10

elif total >= 100 and region == "south":
    discount = 0.07

elif total >= 100:
    discount = 0.05

else:
    discount = 0.02 if region == "south" else 0

final = total * (1 - discount)


print(f"Final discount: {discount * 100:.0f}%")
print(f"Final price: ${final:.2f}")


#--- exercise 2 --- 

if final >= 1000:
    status = "needs_manager_approval"
else:
    status = "auto_approved"

print(f"Status: {status}")


#--- exercise 3 ---

region = "south"

if region == "south":
    print("Region bonus applied: additional 2% off")
else:
    discount = 0.02 if region == "south" else 0

#--- exercise 4 ---
# Flat version
if region == "South" and total > 100 and customer_type == "wholesale":
    extra_discount = 0.03

# The flat version is easier to read and test because all conditions are on one line.
# This makes it clear what must be true for the extra discount to apply.

#--- exercise 5 ---
print("NORMAL") if 1 <= total <= 9999 else print("SUSPICIOUS") if total <= 0 or total <0 else print ("LARGE--REVIEW_REQUIRED") if total >= 10000 else print("INVALID")


#--- exercise 6 --- 
if (total > 2000 or order_count > 10) and not outstanding_balance:
    vip_upgrade = True