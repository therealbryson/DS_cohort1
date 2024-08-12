# Welcome message
# print("Welcome to Python Pizza Deliveries!")

# Prices for pizzas and toppings
small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25
pepperoni_small_price = 2
pepperoni_medium_large_price = 3
extra_cheese_price = 1

# Get user inputs
size = input("What size pizza do you want? Small, Medium, or Large: ").lower()
add_pepperoni = input("Do you want to add pepperoni? 'Y' or 'N': ").upper()
extra_cheese = input("Do you want extra cheese? 'Y' or 'N': ").upper()

# Calculate final bill based on user inputs
bill = 0

if size == "small":
    bill += small_pizza_price
    if add_pepperoni == "Y":
        bill += pepperoni_small_price
elif size == "medium":
    bill += medium_pizza_price
    if add_pepperoni == "Y":
        bill += pepperoni_medium_large_price
elif size == "large":
    bill += large_pizza_price
    if add_pepperoni == "Y":
        bill += pepperoni_medium_large_price

if extra_cheese == "Y":
    bill += extra_cheese_price

# Print the final bill amount
print(f"Your final bill is: ${bill}")
