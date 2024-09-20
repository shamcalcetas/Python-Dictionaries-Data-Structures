# element_symbols_dict.py

# Dictionary of 10 elements and their chemical symbols
element_symbols_dict = {
                          "Hydrogen" : "H",
                          "Helium" : "He",
                          "Lithium" : "Li",
                          "Beryllium" : "Be",
                          "Boron" : "B",
                          "Carbon" : "C",
                          "Nitrogen" : "N",
                          "Gold" : "Au",
                          "Fluorine" : "F",
                          "Neon" : "Ne"
                        }

# Print the entire dictionary
print("10 elements and their chemical symbols: ")
print(element_symbols_dict)

# Access and print the symbol of the 6th element
print()
print("Symbol of the 6th element: ")
print(element_symbols_dict['Carbon'])

# Update the symbol of the 8th element
element_symbols_dict['Gold'] = 'Go'
print()
print("Updated symbol of the 8th element: ")
print(element_symbols_dict)

# Delete the 9th element from the dictionary
del element_symbols_dict['Fluorine']
print()
print("Updated dictionary after deleting 9th element: ")
print(element_symbols_dict)

# Print the last key-value pair in the dictionary
print()
last_key = list(element_symbols_dict.keys())[-1]
last_value = element_symbols_dict[last_key]
print("The last key-value pair is: ")
print(last_key, ":" ,last_value)