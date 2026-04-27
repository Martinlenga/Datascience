# NAME: MARTIN LENGA MWAPAHE

"""
STEPS/PSEUDOCODE:
1. Get inputs (size, toppings, distance)
2. Determine base cost
3. Calculate topping cost
4. Calculate delivery fee
5. Compute total
6. Display result
"""


# Pizza Order Cost Calculator
# This program calculates the total cost of a pizza order
# based on size, toppings, and delivery distance

# Step 1: Get user input
pizza_size = input("Enter pizza size (small/large): ").lower()
toppings = int(input("Enter number of toppings: "))
distance = float(input("Enter delivery distance in miles: "))

# Step 2: Determine base cost
if pizza_size == "small":
    base_cost = 8
elif pizza_size == "large":
    base_cost = 12
else:
    print("Invalid pizza size selected.")
    base_cost = 0

# Step 3: Calculate topping cost
topping_cost = toppings * 1

# Step 4: Calculate delivery fee
if distance <= 5:
    delivery_fee = 2
else:
    delivery_fee = 2 + (distance - 5) * 1

# Step 5: Calculate total cost
total_cost = base_cost + topping_cost + delivery_fee

# Step 6: Display result using f-string
print(f"\nOrder Summary:")
print(f"Pizza Size: {pizza_size}")
print(f"Toppings: {toppings}")
print(f"Delivery Distance: {distance} miles")
print(f"Total Cost: ${total_cost:.2f}")