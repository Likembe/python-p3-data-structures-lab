spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_names = [food["name"] for food in spicy_foods]
    return food_names

result = get_names(spicy_foods)
print(result)

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food ["heat_level"] > 5]
    return spiciest_foods

result = get_spiciest_foods(spicy_foods)
for food in result:
    print(f'Name: {food["name"]}, Cuisine: {food["cuisine"]}, Heat Level: {food["heat_level"]}')



def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"]

        print (f"{name} ({cuisine}) | Heat Level: {heat_level}")

print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
        
    return None
    
cuisine = "American"
result = get_spicy_food_by_cuisine(spicy_foods, cuisine)
if result:
    print(result)
else:
    print(f"No spicy food found with cuisine: {cuisine}")

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = "🌶" * food["heat_level"]  

            print(f"{name} ({cuisine}) | Heat Level: {heat_level}")

print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    num_foods = len(spicy_foods)

    if num_foods == 0:
        return 0  

    average = total_heat / num_foods
    return int(average)

result = get_average_heat_level(spicy_foods)
print(result)

def create_spicy_food(spicy_foods, spicy_food):
    # Create a new list from the existing list to avoid modifying the original list.
    new_spicy_foods_list = spicy_foods.copy()
    new_spicy_foods_list.append(spicy_food)
    return new_spicy_foods_list
