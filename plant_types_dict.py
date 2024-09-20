# plant_types_dict.py

# Dictionary of 8 plants and their types (e.g., shrub, tree, herb)
plant_types_dict = {
                        "Tomato" : "Herbs",
                        "Rose" : "Shrubs",
                        "Grapevine" : "Climbers",
                        "Mango" : "Trees",
                        "Strawberry" : "Creepers",
                        "Sweet gourd" : "Climbers",
                        "Lemon" : "Shrubs",
                        "Watermelon" : "Creepers"
                      }

# Print the entire dictionary
print("8 plants and their types: ")
print(plant_types_dict)

# Access and print the type of the 5th plant
print()
print("Type of the 5th plant: ")
print(plant_types_dict['Strawberry'])

# Update the type of the 2nd plant
plant_types_dict['Rose'] = 'Tree'
print()
print("Updated type of the 2nd plant: ")
print(plant_types_dict)

# Delete the 6th plant from the dictionary
del plant_types_dict['Sweet gourd']
print()
print("Updated dictionary after deleting 6th plant: ")
print(plant_types_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(plant_types_dict.keys())[-1]
last_value = plant_types_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)