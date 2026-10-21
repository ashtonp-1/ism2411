# --- Exercise 5 ---
#type("12") produces the class <class 'str'>, which is a string.
#type(12) produces the class <class 'int'>, which is an integer.
#type(12.0) produces the class <class 'float'>, which is a floating point number.
#type(True) produces the class <class 'bool'>, which is a boolean value.
#'5'+'3 produces the string '53' because both operands are strings, so they are concatenated.
#5+3 produces the integer 8 because both operands are integers, so they are added together.

# --- Exercise 1 ---
products = ("deodorant")
unitprice = 5.99
quantity = 200
in_stock = True
print(type(products), type(unitprice), type(quantity), type(in_stock))

# --- Exercise 2 ---
print(f"{quantity} units of {products} at ${unitprice:.2f} each = ${unitprice * quantity:.2f}") 

# --- Exercise 3 ---
products = input("enter the product name: ")
unitprice = float(input("enter the unit price: "))
quantity = int(input("enter the quantity: "))
print(f"{quantity} units of {products} at ${unitprice:.2f} each = ${unitprice * quantity:.2f}")

# --- Exercise 4 ---
unit_cost = 1.99
revenue = unitprice * quantity
margin = revenue - (unit_cost * quantity)
print(f"products:{products}")
print(f"unit price: ${unitprice:.2f}")
print(f"quantity: {quantity}")
print(f"revenue: ${revenue:.2f}")
print(f"margin: ${margin:.2f}%")