def calculate_cost(hot_dog_type, cheese, peppers, onions):
    if hot_dog_type == "regular":
        base_cost = 3.50
    elif hot_dog_type == "chili":
        base_cost = 4.50
    else:
        return "Invalid hot dog type.", 0, 0  

    toppings_cost = 0.0
    if cheese:
        toppings_cost += 0.50
    if peppers:
        toppings_cost += 0.75
    if onions:
        toppings_cost += 1.00

    total_cost_before_tax = base_cost + toppings_cost

    tax = total_cost_before_tax * 0.07

    total_cost = total_cost_before_tax + tax

    return total_cost_before_tax, tax, total_cost


if __name__ == '__main__':
    hot_dog_type = input("Enter the type of hot dog (regular or chili): ").lower()

    cheese = input("Do you want cheese ($0.50)? (yes or no): ").lower() == "yes"
    peppers = input("Do you want peppers ($0.75)? (yes or no): ").lower() == "yes"
    onions = input("Do you want grilled onions ($1.00)? (yes or no): ").lower() == "yes"

    hot_dog_cost, tax, total_cost = calculate_cost(hot_dog_type, cheese, peppers, onions)

    if hot_dog_cost == "Invalid hot dog type.":
        print("Error: Please enter a valid hot dog type (regular or chili).")
    else:

        print(f"Hot dog cost: ${hot_dog_cost:.2f}")
        print(f"Tax: ${tax:.2f}")
        print(f"Total cost: ${total_cost:.2f}")
