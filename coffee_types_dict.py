# coffee_types_dict.py

# Dictionary of 10 types of coffee and their descriptions
coffee_types_dict = {
                      "Mocha" : "Sweet, nutty and chocolatey",
                      "Macchiato" : "An espresso, topped with a small amount of foamed milk",
                      "Decaf" : "Less caffeine content",
                      "Latte" : "Comprised of a shot of espresso and steamed milk with just a touch of foam",
                      "Black" : "Ground coffee beans steeped in hot water,",
                      "Espresso" : "Served solo or used as the foundation of most coffee drinks",
                      "Cappuccino" : "Latte with more foam than steamed milk, often with a sprinkle of cocoa powder or cinnamon on top",
                      "Irish" : "Consists of black coffee, whiskey and sugar, topped with whipped cream",
                      "Flat White" : "A cappuccino without the foam or chocolate sprinkle with steamed milk",
                      "Affogato" : "Served with a scoop of ice cream and a shot of espresso, or two."
                    }

# Print the entire dictionary
print("10 types of coffee and their descriptions: ")
print(coffee_types_dict)

# Access and print the description of the 4th type of coffee
print()
print("Description of the 4th type of coffee: ")
print(coffee_types_dict['Latte'])

# Update the description of the 8th type of coffee
coffee_types_dict['Irish'] = 'Caffeinated alcoholic drink consisting of Irish whiskey, hot coffee and sugar, which has been stirred and topped with cream'
print()
print("Updated description of the 8th type of coffee: ")
print(coffee_types_dict)

# Delete the 5th type of coffee from the dictionary
del coffee_types_dict['Black']
print()
print("Updated dictionary after deleting 5th type of coffee: ")
print(coffee_types_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(coffee_types_dict.keys())[-1]
last_value = coffee_types_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)