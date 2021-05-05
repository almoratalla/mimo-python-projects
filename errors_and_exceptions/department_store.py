#  Use curly braces to retrieve values from a dict
# floors = ( 
#     "lower": ["clothes", "food"],
#     "upper": ["sports", "shoes"],
#     -1: "gardening", "furniture"
# )
floors = {
    "lower": ["clothes", "food"],
    "upper": ["sports", "shoes"],
    # -1: "gardening", "furniture" - use a proper key and an list value
    "basement": ["gardening", "furniture"]
}

# found = No - should be False instead of No
found = False
requested = "shoes"
current = "ground"

# if requested on floor[current]: - Syntax error, should be in instead of on
if requested in floors[current]:
    print("Yes, on this floor.")
    found = True
else:
    for floor in ["lower", "upper", "basement"]:
        if requested in floors(floor):
            # print("On + floor + floor.") - should use the floor variable
            print("On " + floor + " floor")
            found = True

# if found = False: - should be equality operator instead of assignment
if found == False:
    print("Sorry, not sold in this store.")