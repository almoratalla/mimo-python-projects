menu = ["margherita", "vegetable", "pepperoni"]

# margherita = [0] - needs to be an empty list
margherita = []

vegetable = ["peppers", "mushrooms", "onions"]
pepperoni = ["pepper", "chilli", "salami"]

# Should be a dictionary
# ingredients = (peppers: 0.8 / 
#                 "mushrooms": 0.5,
#                 "onions": 0.6,
#                 "chilli": 0 (free from plant),
#                 "salami": 1.5
# )
ingredients =  {"peppers": 0.8,
                # peppers: 0.8 / - should be string for a key
                "mushrooms": 0.5,
                "onions": 0.6,
                # "chilli": 0 (free from plant), - should be a numerical value
                "chilli": 0, 
                "salami": 1.5
                }

choice = vegetable

base_cost = 2.5
extra_cost = 0

for item in choice:
    # extra_cost = ingredients[item] - should be self incremented
    extra_cost += ingredients[item]

# total_cost = base_cost & extra_cost - total should be a sum of costs
total_cost = base_cost + extra_cost
print(total_cost)