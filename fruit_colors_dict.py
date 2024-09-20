# fruit_colors_dict.py

# Dictionary of 8 fruits and their corresponding colors
fruit_colors_dict = {
                      "Strawberry" : "Red",
                      "Grapes" : "Purple",
                      "Lemon" : "Yellow",
                      "Apple" : "Red",
                      "Orange" : "Orange",
                      "Avocado" : "Green",
                      "Dragon Fruit" : "Pink",
                      "Persimmon" : "Orange"
                    }

# Print the entire dictionary
print("8 fruits and their corresponding colors: ")
print(fruit_colors_dict)

# Access and print the color of the 6th fruit
print()
print("Color of the 6th fruit: ")
print(fruit_colors_dict['Avocado'])

# Update the color of the 4th fruit
fruit_colors_dict['Apple'] = 'Green'
print()
print("Updated color of the 4th fruit: ")
print(fruit_colors_dict)

# Delete the 7th fruit from the dictionary
del fruit_colors_dict['Dragon Fruit']
print()
print("Updated dictionary after deleting 7th fruit: ")
print(fruit_colors_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(fruit_colors_dict.keys())[-1]
last_value = fruit_colors_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)