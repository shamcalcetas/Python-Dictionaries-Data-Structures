# food_recipes_dict.py

# Dictionary of 8 foods and their recipes
food_recipes_dict = {
                      "Grilled Cheese Sandwich" : "Butter bread, place cheese in between, grill both sides until golden brown.",
                      "Scrambled Eggs" : "Beat eggs, add salt & pepper, cook in a pan until set.",
                      "Pasta with Tomato Sauce" : "Cook pasta, heat tomato sauce, mix together.",
                      "Fried Rice" : "Cook rice, stir-fry with eggs, veggies, soy sauce.",
                      "Guacamole" : "Mash avocados, add lime juice, salt, onions, tomatoes.",
                      "Quesadilla" : "Place cheese between tortillas, grill until melted.",
                      "Smoothie" : "Blend fruits, yogurt, and milk until smooth.",
                      "Peanut Butter Toast" : "Toast bread, spread peanut butter.",
                    }

# Print the entire dictionary
print("8 foods and their recipes: ")
print(food_recipes_dict)

# Access and print the recipe of the 5th food
print()
print("Recipe of the 5th food: ")
print(food_recipes_dict['Guacamole'])

# Update the recipe of the 3rd food
food_recipes_dict['Pasta with Tomato Sauce'] = 'Cook pasta, heat canned tomato sauce with your favorite seasonings, then mix together.'
print()
print("Updated recipe of the 3rd food: ")
print(food_recipes_dict)

# Delete the 7th food from the dictionary
del food_recipes_dict['Smoothie']
print()
print("Updated dictionary after deleting 7th food: ")
print(food_recipes_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(food_recipes_dict.keys())[-1]
last_value = food_recipes_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)